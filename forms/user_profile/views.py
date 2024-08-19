from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import forms_page_class


# Create your views here.
def forms_page(request):
    if request.method == 'POST':
        enter_username = request.POST['username']
        print(enter_username)
        if enter_username == "":
            return render(request,'user_profile/forms.html',{
                'haserror':True
            })
        return HttpResponseRedirect('/user/Thanks')
    form = forms_page_class()
    return render(request,'user_profile/forms.html',{'formss':form})
def Thanks(request):
    return render(request,'user_profile/thank_you.html')


