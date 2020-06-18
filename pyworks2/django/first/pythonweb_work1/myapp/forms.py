from django import forms

class TestForm(forms.Form):
    txt = forms.CharField(label = "文字")
    num = forms.IntegerField(label = "数値")


