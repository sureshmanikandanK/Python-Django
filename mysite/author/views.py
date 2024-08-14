from django.shortcuts import render
from django.http import Http404
from .models import author

def author_list(request):
    authors = author.objects.all()
    return render(request, 'author/index.html', {'authors': authors})

# def author_detail(request, author_id):
#         authors = author.objects.get(id=author_id)
#         return render(request, 'author/author_detail.html', {'author': authors})
def author_detail(request,slug):
      authors = author.objects.get(slug=slug)
      return render(request,'author/author_detail.html',{'author':authors})
