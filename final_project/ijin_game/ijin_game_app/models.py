# from django.conf import settings
from django.db import models

from django.contrib.auth.models import AbstractUser

from django.core.validators import FileExtensionValidator
from django.core.validators import RegexValidator


def get_upload_to_user_id_path(instance, filename):
    """イメージアップロード先指定関数

    この関数をImageFieldのupload_toに指定することで、
    ファイルは「MEDIA_ROOT/user/<user_id>/<filename>」にアップロードされる。

    Args:
        instance (FaceURL): FileFieldが定義されているモデルのインスタンス
        filename (str): イメージファイル名

    Returns:
        str: イメージアップロード先パス文字列
    """
    return 'user/{0}/{1}'.format(instance.member, filename)


class Member(AbstractUser):  # バリデーション設定は要相談
    """Memberモデルクラス

    会員登録情報を保存するクラス。

    Djangoがデフォルトで提供している認証システムを使用するため、
    AbstractUserを継承して既存のUserモデルを置き換える。

    会員登録に必要な以下の項目については、デフォルトのUserモデルが既に保持しているFieldであるため、
    Memberクラスでは定義する必要がない。継承したUserモデルのFieldを使用する。
    ・username：ユーザ名(※)
    ・password：パスワード
    ・email：メールアドレス

    ※usernameはUserモデルで定義されているFieldであるが、
    偉人ゲームでは主キーとして使用するため、MemberクラスでField定義を上書きしている。
    本来のUserモデルではidが主キー、usernameはユニークなFieldとして使用されている。

    以下の項目についてはデフォルトのUserモデルが保持していないFieldであるため、Memberクラスで追加する。
    ・nickname：ニックネーム
    ・birthdate：誕生日
    ・belongs_id：所属

    参考：Django の認証方法のカスタマイズ
    https://docs.djangoproject.com/ja/3.0/topics/auth/customizing/

    Args:
        AbstractUser (AbstractUser): 抽象Userクラス
    """
    # 主キーとして利用するためデフォルトUserモデルの username fieldを上書き
    username = models.CharField(
        primary_key=True,
        max_length=150,
        default="",
        verbose_name="ユーザー名"
    )
    nickname = models.CharField(
        max_length=200,
        default=""
    )
    birthdate = models.CharField(
        max_length=200,
        default="",
        validators=[
            RegexValidator(
                r'^\d{4}/\d{1,2}/\d{1,2}$', 'yyyy/MM/dd 形式で入力してください。')
        ]
    )
    belongs_id = models.IntegerField(default=0)


class Belong(models.Model):
    """Belongクラス

    所属を表すデータを保存するクラス。

    会員登録画面上で選択された所属(小学生～社会人)に対応するidと所属名を格納するが、
    AUTO_INCREMENTを設定したカラムで0を使うのは推奨されていない。
    所属の最初は0(小学生)となるため、独自の主キー(belongs_id)を定義する。

    各ユーザの所属についてはMemberクラスのbelongs_idに保存する。
    Belongテーブルには外部キーとしてmember_idを持たない。
    Belongsテーブルは、Memberクラスのbelongs_idに紐づいた所属名を取得する際にJOINして使用する。

    Args:
        models (Model): Django Model クラス
    """
    belongs_id = models.IntegerField(primary_key=True, default=0)
    belongs = models.CharField(max_length=200, default="")


class Playing(models.Model):
    """Playingクラス

    ゲームスコアを保存するクラス。

    Args:
        models (Model): Django Model クラス
    """
    playing_score = models.IntegerField(default=0)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)


class FaceURL(models.Model):
    """FaceURLクラス

    写真登録画面で撮影された顔写真を保存するクラス。

    image_urlには顔写真ファイルのアップロード先パスが保存される。
    顔写真ファイルは「MEDIA_ROOT/user/<user_id>/<filename>」にアップロードされるため、
    そのパスが保存される。(Ex. user/test001/image_1.jpg)

    バリデーションとして、jpg拡張子のファイルのみアップロードを受け付ける。

    Args:
        models (Model): Django Model クラス
    """
    image_url = models.ImageField(
        upload_to=get_upload_to_user_id_path,
        default="",
        validators=[FileExtensionValidator(['jpg', ])],)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
