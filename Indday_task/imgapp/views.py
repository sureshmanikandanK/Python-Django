from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse
from .models import ImgAppDb,Comment
from .forms import post_form
from django.views.generic.edit import CreateView # type: ignore
from django.views.generic import ListView

def land_page(request):
    cards_query = ImgAppDb.objects.all().order_by('-id')[:3]
    section_name = 'Suresh'
    return render(request, 'imgapp/index.html', {'section_name': section_name, 'cards': cards_query, 'showall': False})

def second_page(request):
    cards_query = ImgAppDb.objects.all()
    return render(request, 'imgapp/cards.html', {'cards': cards_query, 'showall': True})

def detail_page(request, slug):
    card = ImgAppDb.objects.filter(slug=slug).first()
    comment=Comment.objects.filter(post_id=card.id)
    return render(request, 'imgapp/detail.html', {'card': card,'comment':comment})


def About_us(request):
    return render(request, 'imgapp/AboutUs.html')

def forms_page(request):
    return render(request, 'imgapp/forms.html')

class commentCreateView(CreateView):
    model = Comment
    template_name = "imgapp/comment.html"
    fields = '__all__'
    success_url ='cards'

class post_page_view(CreateView):
    model = ImgAppDb
    template_name = "imgapp/forms.html"
    fields = ['card_title', 'image', 'card_description', 'author', 'tags']
    success_url ='Add_Cards'


# class post_page_view(View):
#     def get(self, request):
#         form = post_form()
#         return render(request, 'imgapp/forms.html', {'form': form})

#     def post(self, request):
#         submittedform = post_form(request.POST, request.FILES)

#         if submittedform.is_valid():
#             connect = ImgAppDb(
#                 card_title=submittedform.cleaned_data['card_title'],
#                 card_description=submittedform.cleaned_data['card_description'],
#                 image=submittedform.cleaned_data['Image']  
#             )
#             connect.save()
#             return HttpResponseRedirect(reverse('post_page_view'))  
#         else:
#             print(submittedform.errors)  

#         return render(request, 'imgapp/forms.html', {'form': submittedform})