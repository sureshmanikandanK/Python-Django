from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import Profileform
from .models import ProfileImage
from django.views.generic.edit import CreateView # type: ignore
# def store_file(file):
#     with open('temp/userimage.jpg','+wb') as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)
 
class CreateProfileView(View):
    def get(self, request):
        form = Profileform()
 
        return render(request,'profileupload/profile_index.html',{
            'form':form
        })
 
    def post(self, request):
        submittedform = Profileform(request.POST,request.FILES)
 
        if submittedform.is_valid():
            # store_file(request.FILES['userimage'])
            profile = ProfileImage(userimage=request.FILES['userimage'],name=request.FILES['Name'],)
            profile.save()
            return HttpResponseRedirect('/profile')
        return render(request,'profileupload/profile_index.html',{
            'form':submittedform
        })
    
# class CreateProfileView(CreateView):
#     model = ProfileImage
#     template_name = "profileupload/profile_index.html"
#     success_url ='/profile'
#     fields ="__all__"