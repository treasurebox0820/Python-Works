from django import forms

class TestForm(forms.Form):
    txt = forms.CharField(label = "もじ")
    num = forms.IntegerField(label = "すうち")


