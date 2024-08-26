from django import forms

class post_form(forms.Form):
    card_title = forms.CharField(max_length=100)
    card_description = forms.CharField(widget=forms.Textarea)
    Image = forms.FileField()
