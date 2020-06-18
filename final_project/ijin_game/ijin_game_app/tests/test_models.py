from django.test import TestCase
from django.utils import timezone

from ..models import Member

"""test_models.py テストコード実装ルール

    1.models.pyの1つの関数、または1つのクラスにつき、テストクラスを1つ作成する。
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


class MemberModelTests(TestCase):

    def create_member(
            user_id='test_001', password='123456', username='鈴木太郎',
            mailaddress='test@test.com', birthdate='2020/5/12',
            registration_date=timezone.now(), facedata='user/test_001/1.jpeg'):

        return Member(
            user_id, password, username,
            mailaddress, birthdate,
            registration_date, facedata)

    # 現状テストすべき関数がない
