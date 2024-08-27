from django.shortcuts import render
from .models import Post
from django.views import View
from django.views.generic.edit import CreateView # type: ignore
from django.views.generic import ListView
# Create your views here.
def index(request):
    return render(request,'author_app/index.html')

def details(request):
    return render(request,'author_app/POSTDETAILS.html')

class PostListView(ListView):
    model = Post
    template_name = 'author_app/post_list.html'
    context_object_name = 'posts'

class CreateProfileView(CreateView):
    model = Post
    template_name = "author_app/Post_form.html"
    success_url ='postview'
    fields ="__all__"