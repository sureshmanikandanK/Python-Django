from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import forms_page_class

def forms_page(request):
    if request.method == 'POST':
        form = forms_page_class(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/user/Thanks')
    #     else:
    #         return render(request, 'user_profile/forms.html', {
    #             'formss': form,
    #             'formss.user_name.errors':True
    #         })
    # else:
        form = forms_page_class()

        return render(request, 'user_profile/forms.html', {'formss': form})

def Thanks(request):
    return render(request, 'user_profile/thank_you.html')
