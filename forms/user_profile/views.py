from django.shortcuts import render

# Create your views here.
def forms_page(request):
    return render(request,'user_profile/forms.html')