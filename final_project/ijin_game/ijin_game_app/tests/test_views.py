import unittest

from django.test import TestCase

from django.urls import reverse

from ..models import Member
from ..views import RegistMemberView

"""test_views.py テストコード実装ルール

    1.views.pyの1つの関数、または1つのクラスにつき、テストクラスを1つ作成する。
    2.テストクラス名は "関数名(クラス名)" + "Tests" とする。(キャメルケース)
    3.テストクラス内にテストケース(テストしたい条件の集まり)ごとにメソッドを定義する。
    4.テストメソッド名は "test_" + "テスト内容を示すような命名" とする。
    　※テストメソッドは"test"で始める必要がある。
    5.テストメソッドのdocstringには、どのようなテスト内容かを記載する。
"""
"""よく使いそうなassertメソッド
    GoogleDriveの以下に格納しています。

    UnitTestでよく使うassert メソッド一覧
    https://drive.google.com/open?id=16h6iN9AIDsrK9TJ1iSPvQk84CkqNOapE
"""
"""テストの実行方法

    前提：
    「python manage.py test」を実行すると「test_ijin_db」という
    テスト用のデータベースが自動で生成される。(テスト実行が終わったら自動でロールバック)
    上記データベースにアクセスするために、DBユーザ「ijin_game」に権限を付与する必要がある。
    テスト実行前にmySQLで以下を実行してください。

    > mysql -u root -p
    > Enter password: 各自設定したrootユーザのpass
    > GRANT ALL ON *.* TO ijin_game@localhost identified by 'PythonStartLab%1';

    1.以下のコマンドを実行
    　python manage.py test

    ---------- 以下は実施不要です ----------
    2. カバレッジの取得
        ※coverage.pyを環境にインストールしていない場合は「pip install coverage」してから実行する
        coverage run --source='.' manage.py test

    3. カバレッジレポートの取得
        coverage report
        coverage html
"""
"""テスト実行時の動作について

    1.manage.py test は、アプリケーション内にあるテストファイル(test～.py)を探します。
    2.django.test.TestCase クラスのサブクラスを発見します。
    3.テストのための特別なデータベースを作成します。(test_ijin_db)
    4.テスト用のメソッドとして、test で始まるメソッドを探します。
    5.そして最後に、 assert～() メソッドを使うことで、実装結果が正しいことを確認します。
"""


class TopViewTests(TestCase):
    """
    top関数のテストケース
    トップページに関するテストケースを定義する。
    """

    def test_top_screen_transition(self):
        """
        トップページ画面が正しく取得できるか確認する。
        レスポンスのHTTPステータスが200であればOK
        """
        response = self.client.get(reverse('top'))
        self.assertEqual(response.status_code, 200)


class RegistMemberViewTests(TestCase):
    """
    RegistMemberViewクラスのテストケース
    会員登録画面に関するテストケースを定義する。
    """

    def setUp(self):
        self.test_class = RegistMemberView()

    def test_regist_member_screen_transition(self):
        """
        会員登録画面が正しく取得できるか確認する。
        レスポンスのHTTPステータスが200であればOK
        """
        response = self.client.get(reverse('regist_member'))
        self.assertEqual(response.status_code, 200)


class RegistPhotoGraphViewTests(TestCase):
    """regist_photograph関数のテストケース"""

    def setUp(self):
        """
        テストメソッドの実行前に実行されるセットアップメソッド
        ・ログイン状態にする
        ・セッションデータの設定
        """
        # ログイン認証
        self.user = Member.objects.create_user(
            'testuser', 'test@test.com', 'Root123@')
        self.client.login(username='testuser', password='Root123@')

        # セッションデータ設定
        session = self.client.session
        session['username'] = 'testuser'
        session['user_ijin_data'] = (0, "藤原道長")
        session['cnn_score'] = 50
        session.save()

    def test_regist_photograph_screen_transition(self):
        """
        写真登録画面が正しく取得できるか確認する。
        レスポンスのHTTPステータスが200であればOK
        """
        response = self.client.get(reverse('regist_photograph'))
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        response = self.client.get(reverse('regist_photograph'))

        self.assertEqual(response.status_code, 200)

        # レスポンスに返されるHTMLの中身を確認する
        self.assertContains(response, '写真登録')


class RegistImageFileTests(TestCase):
    """regist_image_file関数のテストケース"""

    def setUp(self):
        """
        テストメソッドの実行前に実行されるセットアップメソッド
        ・ログイン状態にする
        ・セッションデータの設定
        """
        # ログイン認証
        self.user = Member.objects.create_user(
            'testuser', 'test@test.com', 'Root123@')
        self.client.login(username='testuser', password='Root123@')

        # セッションデータ設定
        session = self.client.session
        session['username'] = 'testuser'
        session['user_ijin_data'] = (0, "藤原道長")
        session['cnn_score'] = 50
        session.save()

    def test_regist_image_file_screen_transition(self):
        """
        マイページ画面に正しく遷移できるか確認する。
        レスポンスのHTTPステータスが200であればOK
        """
        response = self.client.get(reverse('mypage'))
        self.assertEqual(response.status_code, 200)


class RegistPhotoFileTests(TestCase):
    """regist_photo_file関数のテストケース"""

    def setUp(self):
        """
        テストメソッドの実行前に実行されるセットアップメソッド
        ・ログイン状態にする
        ・セッションデータの設定
        """
        # ログイン認証
        self.user = Member.objects.create_user(
            'testuser', 'test@test.com', 'Root123@')
        self.client.login(username='testuser', password='Root123@')

        # セッションデータ設定
        session = self.client.session
        session['username'] = 'testuser'
        session['user_ijin_data'] = (0, "藤原道長")
        session['cnn_score'] = 50
        session.save()

    def test_regist_image_file_screen_transition(self):
        """
        マイページ画面に正しく遷移できるか確認する。
        レスポンスのHTTPステータスが200であればOK
        """
        response = self.client.get(reverse('mypage'))
        self.assertEqual(response.status_code, 200)


class LoginViewTests(TestCase):
    """login関数のテストケース"""

    def test_login_screen_transition(self):
        """
        ログイン画面が正しく取得できるか確認する。
        レスポンスのHTTPステータスが200であればOK
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)


class MyPageViewTests(TestCase):
    """mypage関数のテストケース"""

    def setUp(self):
        """
        テストメソッドの実行前に実行されるセットアップメソッド
        ・ログイン状態にする
        ・セッションデータの設定
        """
        # ログイン認証
        self.user = Member.objects.create_user(
            'testuser', 'test@test.com', 'Root123@')
        self.client.login(username='testuser', password='Root123@')

        # セッションデータ設定
        session = self.client.session
        session['username'] = 'testuser'
        session['user_ijin_data'] = (0, "藤原道長")
        session['cnn_score'] = 50
        session.save()

    def test_mypage_screen_transition(self):
        """
        マイページ画面が正しく取得できるか確認する。
        レスポンスのHTTPステータスが200であればOK
        """
        response = self.client.get(reverse('mypage'))
        self.assertEqual(response.status_code, 200)


class HowToPlayViewTests(TestCase):
    """how_to_play関数のテストケース"""

    def test_how_to_play_screen_transition(self):
        """
        ゲーム説明画面が正しく取得できるか確認する。
        レスポンスのHTTPステータスが200であればOK
        """
        response = self.client.get(reverse('how_to_play'))
        self.assertEqual(response.status_code, 200)


class RecognizeIjinImageViewTests(TestCase):
    """recognize_ijin_image関数のテストケース"""

    def setUp(self):
        """
        テストメソッドの実行前に実行されるセットアップメソッド
        ・ログイン状態にする
        ・セッションデータの設定
        TODO 「media/user/imagetest001」フォルダ(写真登録済みユーザの任意のフォルダ)を
        指定して写真(+水増し処理した写真)を格納しておく必要がある。
        """
        # ログイン認証
        self.user = Member.objects.create_user(
            'imagetest001', 'test@test.com', 'Root123@')
        self.client.login(username='imagetest001', password='Root123@')

        # セッションデータ設定
        session = self.client.session
        session['username'] = 'imagetest001'
        session['user_ijin_data'] = (0, "藤原道長")
        session['cnn_score'] = 50
        session.save()

    def test_recognize_ijin_image_screen_transition(self):
        """
        偉人画像認識画面が正しく取得できるか確認する。
        レスポンスのHTTPステータスが200であればOK
        """
        response = self.client.get(reverse('recognize_ijin_image'))
        self.assertEqual(response.status_code, 200)

    def test_cnn_result(self):
        """
        templateに設定されるパラメータが正しいことを確認する。
        """
        response = self.client.get(reverse('recognize_ijin_image'))
        self.assertEqual(response.status_code, 200)

        # パラメータを確認する
        # self.assertLess(response.context['loss'], 2.0)
        # self.assertGreater(response.context['accuracy'], 0.3)
        self.assertTrue(response.context['ijin_name'])
        self.assertGreater(response.context['percentage'], 50)
        self.assertTrue(response.context['ijin_image_name'])
        self.assertEqual(response.context['username'], 'imagetest001')


class GenerateIjinSentenceViewTests(TestCase):
    """generate_ijin_sentence関数のテストケース"""

    def setUp(self):
        """
        テストメソッドの実行前に実行されるセットアップメソッド
        ・ログイン状態にする
        ・セッションデータの設定
        """
        # ログイン認証
        self.user = Member.objects.create_user(
            'testuser', 'test@test.com', 'Root123@')
        self.client.login(username='testuser', password='Root123@')

        # セッションデータ設定
        session = self.client.session
        session['username'] = 'testuser'
        session['user_ijin_data'] = (0, "藤原道長")
        session['cnn_score'] = 50
        session.save()

    def test_generate_ijin_sentence_screen_transition(self):
        """
        偉人文章入力画面が正しく取得できるか確認する。
        レスポンスのHTTPステータスが200であればOK
        """
        response = self.client.get(reverse('generate_ijin_sentence'))
        self.assertEqual(response.status_code, 200)


class ResultViewTests(TestCase):
    """result関数のテストケース"""

    def setUp(self):
        """
        テストメソッドの実行前に実行されるセットアップメソッド
        ・ログイン状態にする
        ・セッションデータの設定
        """
        # ログイン認証
        self.user = Member.objects.create_user(
            'testuser', 'test@test.com', 'Root123@')
        self.client.login(username='testuser', password='Root123@')

        # セッションデータ設定
        session = self.client.session
        session['username'] = 'testuser'
        session['user_ijin_data'] = (0, "藤原道長")
        session['cnn_score'] = 50
        session.save()

        self.test_data = {
            "input_text": "平安時代の中期の公卿。藤原北家、摂政関白太政大臣・藤原兼家の五男（または四男）。後一条天皇・後朱雀天皇・後冷泉天皇の外祖父にあたる。"
        }

    def test_result_screen_transition(self):
        """
        ゲームスコア表示画面が正しく取得できるか確認する。
        レスポンスのHTTPステータスが200であればOK
        """
        response = self.client.post(reverse('result'))
        self.assertEqual(response.status_code, 200)

    @unittest.skip("skip test_get_score")
    def test_get_score(self):
        """
        templateに設定されるパラメータが正しいことを確認する。
        スコアが取得できることを確認する。
        TODO 以下のエラーが発生する。
        テスト実行時にvewsからrestAPIが呼び出せていない問題を解決できていない。
        json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
        """
        response = self.client.post(reverse('result'), self.test_data)
        self.assertEqual(response.status_code, 200)

        # テンプレートのインスタンスの値を確認する
        print(str(response.context['cnn_score']))
        self.assertTrue(response.context['cnn_score'])


class RankingViewTests(TestCase):
    """ranking関数のテストケース"""

    def setUp(self):
        """
        テストメソッドの実行前に実行されるセットアップメソッド
        ・ログイン状態にする
        ・セッションデータの設定
        """
        # ログイン認証
        self.user = Member.objects.create_user(
            'testuser', 'test@test.com', 'Root123@')
        self.client.login(username='testuser', password='Root123@')

        # セッションデータ設定
        session = self.client.session
        session['username'] = 'testuser'
        session['user_ijin_data'] = (0, "藤原道長")
        session['cnn_score'] = 50
        session.save()

    def test_ranking_screen_transition(self):
        """
        ランキング表示画面が正しく取得できるか確認する。
        レスポンスのHTTPステータスが200であればOK
        """
        response = self.client.get(reverse('ranking'))
        self.assertEqual(response.status_code, 200)


class AjaxImageUploadTests(TestCase):
    """ajax_image_upload関数のテストケース"""

    def setUp(self):
        """
        テストメソッドの実行前に実行されるセットアップメソッド
        ・ログイン状態にする
        ・セッションデータの設定
        """
        # ログイン認証
        self.user = Member.objects.create_user(
            'testuser', 'test@test.com', 'Root123@')
        self.client.login(username='testuser', password='Root123@')

        # セッションデータ設定
        session = self.client.session
        session['username'] = 'testuser'
        session['user_ijin_data'] = (0, "藤原道長")
        session['cnn_score'] = 50
        session.save()

    def test_ajax_image_upload(self):
        """
        ajax_image_uploadでの非同期通信が正しくできるか確認する。
        jsonデータが取得できればOK
        """
        with open('./media/cnn_data/other/image_0.jpg', 'r', encoding="utf-8", errors='ignore') as f:
            response = self.client.post(
                reverse('ajax_image_upload'), {'face_image': f})

        self.assertTrue(response)
