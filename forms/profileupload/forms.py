from django import forms
class Profileform(forms.Form):
    userimage = forms.FileField()