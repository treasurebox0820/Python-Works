import json

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import FormView

import requests

from .models import FaceURL
from .models import Playing

from .forms import CreateForm
from .forms import ImageFileUploadForm
from .forms import InputIjinSentenseForm

from .views_functions.image_analysis import data_aug
from .views_functions.image_analysis import cnn_ijin_loadmodel


def top(request):
    """トップページ

    「Youはなにした偉人さん？」アプリにアクセスした際に最初に表示される画面

    Args:
        request (HttpRequest): リクエスト

    Returns:
        [HttpResponse]: レスポンス
    """
    return render(request, 'top.html')


class RegistMemberView(FormView):
    """会員登録

    会員登録画面はDjangoの汎用ビューであるFormViewを
    継承したクラスベースとして作成する。

    form_class    : 会員登録画面で使用するFormクラス
    template_name : 会員登録画面で使用するtemplate
    success_url   : 遷移先URL(reverse_lazyで遅延評価)

    Args:
        FormView (FormView): クラスベースGenericView
    """
    form_class = CreateForm
    template_name = 'regist_member.html'
    success_url = reverse_lazy('regist_photograph')


def regist_photograph(request):
    """写真登録

    画像解析に使用する写真を撮影する画面

    Args:
        request (HttpRequest): リクエスト

    Returns:
        [HttpResponse]: レスポンス
    """
    if request.method == 'POST':
        create_form = CreateForm(request.POST)

        if create_form.is_valid():
            create_form.save()

            # 引数で渡したIDとPWが一致するユーザインスタンスを返す
            authed_member = authenticate(  # 認証
                username=create_form.cleaned_data['username'],
                password=create_form.cleaned_data['password1'],
            )

            # ログイン
            auth_login(request, authed_member)

            # usernameをセッションに保持
            request.session['username'] = create_form.cleaned_data['username']

        else:
            print('error')
            return render(request, 'regist_member.html', {'form': create_form})

    return render(request, 'regist_photograph.html', {'form': ImageFileUploadForm()})


@login_required
def regist_image_file(request):
    """写真ファイル登録

    写真登録画面でローカルよりファイルを選択してファイル登録した際に呼び出される処理。
    ブラウザで写真撮影した場合は「regist_photo_file()」が呼び出されるため、実装時には注意する。

    Args:
        request (HttpRequest): リクエスト

    Returns:
        HttpResponse: レスポンス
    """
    if request.method == 'POST':
        username = request.session.get('username')

        # 選択したファイルを「/media/user/<username>」にアップロードし、そのPathをFaceURLテーブルに保存
        image_form = ImageFileUploadForm(request.POST, request.FILES)
        if image_form.is_valid():
            images = request.FILES.getlist('image_url', False)
            for image in images:
                image_url = FaceURL.objects.create(
                    member_id=username, image_url=image)
                image_url.save()

            # データ拡張
            print('run data_aug.augument_data() : 画像データ拡張を実行中...')
            data_aug.augument_data(username)

            # マイページにリダイレクト
            return HttpResponseRedirect(reverse('mypage'))
        else:
            print(image_form.errors)

    return render(request, 'regist_photograph.html', {'form': image_form})


@login_required
def regist_photo_file(request):
    """ブラウザ撮影写真登録

    写真登録画面でPCカメラを使用して写真撮影を行い、写真登録した際に呼び出される処理。
    写真ファイルをローカルから選択した場合は「regist_image_file()」が呼び出されるため、実装時には注意する。

    また、ブラウザで撮影した写真は当該関数ではなく
    「ajax_image_upload()」関数を使用し、ajaxを利用してアップロードしている。

    Args:
        request (HttpRequest): リクエスト

    Returns:
        HttpResponse: レスポンス
    """
    if request.method == 'POST':
        username = request.session.get('username')

        # データ拡張
        print('run data_aug.augument_data() : 画像データ拡張を実行中...')
        data_aug.augument_data(username)

        # マイページにリダイレクト
        return HttpResponseRedirect(reverse('mypage'))

    return render(request, 'regist_photograph.html', {'form': ImageFileUploadForm()})


@login_required
def mypage(request):
    """マイページ

    ユーザのマイページを表示する画面

    Args:
        request (HttpRequest): リクエスト

    Returns:
        [HttpResponse]: レスポンス
    """
    # ログインユーザをセッションに保持
    if request.user.is_authenticated:
        # print('Login User : ', request.user.username)
        request.session['username'] = request.user.username

    return render(request, 'mypage.html')


def how_to_play(request):
    """ゲーム説明

    ゲームの遊び方を表示する画面

    Args:
        request (HttpRequest): リクエスト

    Returns:
        [HttpResponse]: レスポンス
    """

    return render(request, 'how_to_play.html')


# 偉人の辞書{キーワード:(ID, 名前)}テスト用でnarusawaも
ijin_dict = {"fujiwara": (0, "藤原道長"), "minamoto": (1, "源頼朝"), "oda": (2, "織田信長"), "saigo": (3, "西郷隆盛"),
             "tenji": (4, "天智天皇"), "taira": (5, "平清盛"), "tokugawa": (6, "徳川家康"), "toyotomi": (7, "豊臣秀吉"),
             "sakamoto": (8, "坂本龍馬"), "date": (9, "伊達政宗"), "natume": (10, "夏目漱石"), "noguchi": (11, "野口英世"),
             "rikyu": (12, "千利休"), "ito": (13, "伊藤博文"), "katsu": (14, "勝海舟"), "shotoku": (15, "聖徳太子"),
             "ashikaga": (16, "足利義満"), "itagaki": (17, "板垣退助"), "iwakura": (18, "岩倉具視"), "inou": (19, "伊能忠敬"),
             "narusawa": (20, "narusawa")}


@login_required
def recognize_ijin_image(request):
    """偉人画像認識

    ユーザの写真を解析しどの偉人と類似しているか判定する画面

    Args:
        request (HttpRequest): リクエスト

    Returns:
        [HttpResponse]: レスポンス
    """
    # セッションからusernameを取得
    username = request.session.get('username')

    # 画像認識
    # user_ijin = cnn_ijin.predict_ijin(username)

    # 転移学習利用の場合、こちらを有効にし、上はコメントアウトで
    user_ijin = cnn_ijin_loadmodel.predict_ijin(username)

    cnn_result_dict = {
        # 'loss': score[0],
        # 'accuracy': score[1],
        'ijin_name': ijin_dict[user_ijin[0]][1],
        'percentage': int(round(user_ijin[1] * 100, 0)),
        'ijin_image_name': user_ijin[0],
        'username': username,
    }

    # セッションにデータ保持:偉人データ(偉人ID, 偉人名)
    request.session['user_ijin_data'] = ijin_dict[user_ijin[0]]
    # cnn_result_dictのpercentageキーの値
    request.session["cnn_score"] = int(round(user_ijin[1] * 100, 0))

    return render(request, 'recognize_ijin_image.html', cnn_result_dict)


@login_required
def generate_ijin_sentence(request):
    """偉人文章入力

    類似する偉人に関する文章を入力する画面

    Args:
        request (HttpRequest): リクエスト

    Returns:
        [HttpResponse]: レスポンス
    """
    # セッションからデータ取得
    user_ijin = request.session.get('user_ijin_data')
    # print('セッションから取得した偉人データ : ', user_ijin)

    # user_ijin = (
    #     'natume', 3)  # ダミーデータ # score, user_ijin = cnn_ijin.predict_ijin()
    input_dict = {
        'form': InputIjinSentenseForm(),
        'ijin_name': user_ijin[1]
        # 'ijin_name': ijin_dict[user_ijin[0]][1]
    }
    return render(request, 'generate_ijin_sentence.html', input_dict)


@login_required
def result(request):
    """ゲームスコア表示

    偉人の類似度と偉人に関する文章入力の結果としてスコアを表示する画面

    Args:
        request (HttpRequest): リクエスト

    Returns:
        [HttpResponse]: レスポンス
    """

    # POSTのときのみ、リクエストからデータを取得
    if (request.method == "POST"):

        # セッションからデータ取得
        user_ijin = request.session.get('user_ijin_data')
        cnn_score = request.session.get("cnn_score")
        # print('セッションから取得した偉人データ : ', user_ijin)
        # print('セッションから取得したCNNのスコア : ', cnn_score)

        ijin_name = user_ijin[1]
        input_form = InputIjinSentenseForm(request.POST)

        if input_form.is_valid():

            input_text = input_form.cleaned_data["input_text"]

            # APIアプリに渡すJSON形式データを生成
            api_request_dict = json.dumps(
                {"ijin_name": ijin_name, "input_text": input_text})

            # APIアプリにデータを渡して受け取る
            api_response = requests.post(
                request.build_absolute_uri(
                    reverse("syntactic_analysis")),
                api_request_dict,
                headers={"content-Type": "application/json"}
            )

            # APIアプリから受け取ったデータをJSONからデコードする
            # nlp_result_dict = json.loads(api_response)
            nlp_result_dict = api_response.json()
            # nlp_result_dict は {"score":50, "ijin_name": "夏目漱石"}

            # TODO DB担当と確認する
            # 構文解析結果をテーブルに保存(必要であれば)
            # ユーザの最高得点データと比較して、本スコアの方が高ければ、更新して保存する、か？
            # if user.highest_score < nlp_result_dict["score"]: ??
            # user.highest_score = nlp_result_dict["score"] ??
            # user.save() ??

            nlp_result_dict["cnn_score"] = cnn_score
            nlp_result_dict["total_score"] = int(
                nlp_result_dict["score"]) + int(nlp_result_dict["cnn_score"])

            username = request.session.get('username')

            score = Playing.objects.create(member_id=username)
            score.playing_score = nlp_result_dict["total_score"]
            score.save()

            # テンプレ表示用
            nlp_result_dict["ijin_name"] = ijin_name

            # TODO スコアの大きさに応じてmessageを変える
            if nlp_result_dict["total_score"] > 160:
                message = f"Youの{nlp_result_dict['ijin_name']}のなりきり具合は、もはや物マネではなく天性のものに違いない。{nlp_result_dict['ijin_name']}の生まれ変わりとして偉大な活躍することができるでしょう！"

            elif nlp_result_dict["total_score"] > 140:
                message = f"Youの{nlp_result_dict['ijin_name']}のなりきり具合は一般人とは思えない！物まねのプロとして世界に羽ばたくでしょう！もっと知識を増やせば更に偉大な活躍が君を待っている！"

            else:
                message = f"Youは{nlp_result_dict['ijin_name']}にちょっと似ている人として、学園祭で拍手喝采間違いなし！もう少し顔を似せるか知識を増やせば、更なる活躍が期待できるでしょう！"
            nlp_result_dict["message"] = message

            # テストの代わりにコンソールに出力して確認
            # print("nlp_result_dict['form']['score']", nlp_result_dict["score"])
            # print("nlp_result_dict['form']['cnn_score']",
            #       nlp_result_dict["cnn_score"])
            # print("nlp_result_dict['form']['total_score']",
            #       nlp_result_dict["total_score"])
            # print("nlp_result_dict['form']['message']",
            #       nlp_result_dict["message"])
            # print("inlp_result_dict['ijin_name']",
            #       nlp_result_dict["ijin_name"])

            return render(request, 'result.html', nlp_result_dict)

        # 入力が10文字未満、1000文字以上の場合：
        else:
            input_dict = {
                'form': input_form,
                'ijin_name': user_ijin[1],
            }

            return render(request, "generate_ijin_sentence.html", input_dict)

    # POST以外のリクエストへの対応
    else:
        abc = 1


@ login_required
def ranking(request):
    """ランキング

    スコアのランキングを表示する画面

    Args:
        request (HttpRequest): リクエスト

    Returns:
        [HttpResponse]: レスポンス
    """
    playing_score = Playing.objects.order_by("-playing_score")
    all_member = []
    for data in playing_score:
        user_dict = {}
        user_dict["user"] = data.member_id
        user_dict["score"] = data.playing_score
        all_member.append(user_dict)
    return render(request, 'ranking.html', {'all_member': all_member})


@ login_required
def ajax_image_upload(request):
    """撮影画像のアップロードを行うajax関数

    非同期処理のため、face_urlテーブルに格納される
    idとimage_urlのファイル名番号は必ずしも一致しない。

    Args:
        request ([type]): リクエスト

    Returns:
        JsonResponse: JSON形式のレスポンス
    """
    username = request.session.get('username')
    image_file = request.FILES['face_image']

    image_url = FaceURL.objects.create(
        member_id=username, image_url=image_file)
    image_url.save()

    result = {
        # 画像のアップロードが成功したらファイル名を返却
        'file_name': str(image_file),
    }

    return JsonResponse(result)
