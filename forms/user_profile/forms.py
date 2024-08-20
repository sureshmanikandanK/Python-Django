from django import forms
 
class forms_page_class(forms.Form):
    user_name = forms.CharField(label= 'Enter Your Name : ',max_length=20,required=False,
        error_messages={'required': 'Please enter your name.'})