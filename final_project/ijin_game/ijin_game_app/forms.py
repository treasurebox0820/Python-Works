from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from .models import Member
from .models import FaceURL


class CreateForm(UserCreationForm):
    """会員登録Form

    会員登録を行うクラス。

    新しいユーザを作成するためのModelFormであるUserCreationFormを継承している。
    UserCreationFormは3つのフィールドが存在する(username、password1、password2)。
    password1 と password2 が一致するか確認し、validate_password() を使ってパスワードを検証する。
    そして、set_password() を使ってユーザのパスワードをセットする。

    UserCreationFormで未定義の項目やFieldのカスタマイズをCreateFormで行っている。

    Args:
        UserCreationForm (UserCreationForm): [description]
    """

    def __init__(self, *args, **kwargs):
        """初期化メソッド

        UserCreationFormの__init__()を呼び出した後、全Fieldに共通の定義を行っている。
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'  # クラス属性の指定
            field.widget.attrs['required'] = True  # 必須項目として指定

    class Meta:
        """Metaクラス

        CreateFormのメタデータを定義する。

        model   : メタクラスとしてMemberモデルを指定する。
        fields  : Formとして画面に表示するFieldを指定する。
        labels  : 各Fieldの画面表示時のラベルを指定する。
        widgets : 各Fieldに適用するウィジェットを指定する。
        """
        model = Member
        fields = UserCreationForm.Meta.fields + \
            ('email', 'nickname', 'birthdate', 'belongs_id')

        labels = {
            'username': 'ユーザー名',
            'nickname': 'ニックネーム',
            'birthdate': '誕生日',
        }

        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Ex. test001', }),
            'password1': forms.PasswordInput(
                attrs={'placeholder': 'Ex. Root123@', }),
            'password2': forms.PasswordInput(
                attrs={'placeholder': 'Ex. Root123@', }),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Ex. test@test.com', }),
            'nickname': forms.TextInput(
                attrs={'placeholder': 'Ex. テスト', }),
            'birthdate': forms.DateInput(
                attrs={'placeholder': 'Ex. 2020/05/18', }),
        }

    # 所属はフォームフィールド自体を変更するため(IntegerField → ChoiceField)
    # Metaクラスではなくここで上書き
    CHOICES = (
        ('0', '小学生'),
        ('1', '中学生'),
        ('2', '高校生'),
        ('3', '大学生'),
        ('4', '社会人'),
    )

    belongs_id = forms.ChoiceField(
        label='所属',
        widget=forms.RadioSelect(),
        choices=CHOICES,
        required=True,
        initial=0
    )


class ImageFileUploadForm(forms.ModelForm):
    """画像ファイルアップロードForm

    画像ファイルのアップロードを行うクラス。
    写真登録画面でブラウザで撮影した写真ではなく、
    ファイルを選択してアップロードした場合に当該Formが呼び出される。

    Args:
        forms (ModelForm): Model Form
    """
    class Meta:
        """Metaクラス

        ImageFileUploadFormのメタデータを定義する。

        model   : メタクラスとしてFaceURLモデルを指定する。
        fields  : Formとして画面に表示するFieldを指定する。
        widgets : 各Fieldに適用するウィジェットを指定する。
        """
        model = FaceURL
        fields = ('image_url',)

        widgets = {
            'image_url': forms.ClearableFileInput(attrs={'multiple': True}),
        }

    def clean_image_url(self):
        """image_url:画像ファイルURLのバリデーション設定メソッド

        Raises:
            ValidationError: 選択された写真ファイル数が10枚より少ない場合はエラー
            ValidationError: 選択された写真ファイル数が20枚を超える場合はエラー

        Returns:
            image_url: 画像ファイルURL
        """
        image_url_list = self.files.getlist('image_url')
        if len(image_url_list) < 10:
            raise ValidationError('選択する写真は10枚以上にしてください。')

        if 20 < len(image_url_list):
            raise ValidationError('選択する写真は20枚以下にしてください。')

        image_url = self.cleaned_data['image_url']
        return image_url


class InputIjinSentenseForm(forms.Form):
    input_text = forms.CharField(
        label='コメント',
        required=True,
        widget=forms.Textarea(
            attrs={'cols': '50', 'rows': '6', 'class': 'form-control'}
        ),
        # TODO 文字数が10文字未満、1000文字以上であれば、同画面にrenderするが、
        # messageをテンプレートに表示することができなかったため、改良が必要。
        validators=[
            validators.MaxLengthValidator(1000, message='文章は最大1000文字までだよ'),
            validators.MinLengthValidator(10, message='文章は最低10文字以上書いてね！'),
        ]
    )
