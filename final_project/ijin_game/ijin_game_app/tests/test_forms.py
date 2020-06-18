import unittest

from django.test import TestCase

from ..forms import CreateForm, InputIjinSentenseForm
from ..models import Member, FaceURL

"""test_forms.py テストコード実装ルール

    1.forms.pyの1つの関数、または1つのクラスにつき、テストクラスを1つ作成する。
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


class CreateFormTests(TestCase):
    """
    CreateFormクラスのテストケース
    会員登録Formに関するテストケースを定義する。
    """

    def setUp(self):
        self.member = Member.objects.create(
            username='test_user', password='Root123@', email='test@test.com',
            nickname='test', birthdate='2020/05/18', belongs_id=0)

        self.test_data = {
            'username': self.member.pk,
            'password1': self.member.password,
            'password2': self.member.password,
            'email': self.member.email,
            'nickname': self.member.nickname,
            'birthdate': self.member.birthdate,
            'belongs_id': self.member.belongs_id,
        }

    def test_normal(self):
        """正常系のテスト"""
        form = CreateForm(self.test_data, instance=self.member)
        self.assertTrue(form.is_valid())

    def test_username_no_required(self):
        """
        username：
        必須項目であることの確認
        """
        self.test_data['username'] = ''
        form = CreateForm(self.test_data, instance=self.member)
        self.assertFalse(form.is_valid())

    @unittest.skip("test_username_duplicate")
    def test_username_duplicate(self):
        """
        username：
        一意制約(重複登録を許可しない)の確認
        TODO 一意制約を確認できていない
        """
        form = CreateForm(self.test_data, instance=self.member)
        form.save()
        self.test_data['username'] = 'test_user'
        form2 = CreateForm(self.test_data, instance=self.member)
        form2.save()
        self.assertTrue(form2.is_valid())


class ImageFileUploadFormTests(TestCase):
    """
    ImageFileUploadFormクラスのテストケース
    画像ファイルアップロードFormに関するテストケースを定義する。
    """

    def setUp(self):
        self.face_url = FaceURL.objects.create(
            id=0, image_url='user/test_user/image_0.jpg', member_id='test_user')

        self.test_data = {
            'id': self.face_url.pk,
            'image_url': self.face_url.image_url,
            'member_id': self.face_url.member_id,
        }

    # TODO ファイル数に関するテスト


class InputIjinSentenseFormTests(TestCase):
    """
    InputIjinSentenseFormクラスのテストケース
    偉人文章入力Formに関するテストケースを定義する。
    """

    def setUp(self):
        self.test_data = {
            'input_text': 'あいうえおかきくけこ',
        }

    def test_input_text_normal(self):
        """入力テキストが10文字以上1000文字以下"""

        self.test_data = {
            'input_text': 'あいうえおあいうえお',
        }

        form = InputIjinSentenseForm(self.test_data)
        self.assertTrue(form.is_valid())

    def test_input_text_less_than(self):
        """入力テキストが10文字より少ない"""

        self.test_data = {
            'input_text': 'あいうえおあいうえ',
        }

        form = InputIjinSentenseForm(self.test_data)
        self.assertFalse(form.is_valid())

    def test_input_text_greater_than(self):
        """入力テキストが1000文字を超える"""

        self.test_data = {
            'input_text': '''
            あいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえお
            あいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえお
            あいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえお
            あいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえお
            あいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえお
            あいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえお
            あいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえお
            あいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえお
            あいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえお
            あいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえお
            あ
            ''',
        }

        form = InputIjinSentenseForm(self.test_data)
        self.assertFalse(form.is_valid())
