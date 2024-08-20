from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import forms_page_class
from .models import Review

def forms_page(request):
    if request.method == 'POST':
        form = forms_page_class(request.POST)
        if form.is_valid():
            review = Review(
                user_name = form.cleaned_data['user_name'],
                text = form.cleaned_data['text'],
                rating = form.cleaned_data['rating'],
            )
            review.save()
            return HttpResponseRedirect('/user/Thanks')
    else:
        form = forms_page_class()
        return render(request, 'user_profile/forms.html', {'form': form})

def Thanks(request):
    return render(request, 'user_profile/thank_you.html')
