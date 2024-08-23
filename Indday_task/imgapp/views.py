from django.shortcuts import render
from .models import ImgApp

# Mock data
# cards_data = [
#     {'id': 1, 'card_title': 'Card 1', 'card_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla consectetur tortor vel magna tincidunt tempus. Maecenas eget maximus eros. Vivamus id nisl lacus. Donec et risus turpis. In nec efficitur purus, ac faucibus nulla.', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmCy16nhIbV3pI1qLYHMJKwbH2458oiC9EmA&s'},
#     {'id': 2, 'card_title': 'Card 2', 'card_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla consectetur tortor vel magna tincidunt tempus. Maecenas eget maximus eros. Vivamus id nisl lacus. Donec et risus turpis. In nec efficitur purus, ac faucibus nulla.', 'image': 'https://images.ctfassets.net/hrltx12pl8hq/28ECAQiPJZ78hxatLTa7Ts/2f695d869736ae3b0de3e56ceaca3958/free-nature-images.jpg?fit=fill&w=1200&h=630'},
#     {'id': 3, 'card_title': 'Card 3', 'card_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla consectetur tortor vel magna tincidunt tempus. Maecenas eget maximus eros. Vivamus id nisl lacus. Donec et risus turpis. In nec efficitur purus, ac faucibus nulla.', 'image': 'https://cdn.pixabay.com/photo/2024/05/26/10/15/bird-8788491_1280.jpg'},
# ]

def land_page(request):
    cards_query = ImgApp.objects.all().order_by('-id')[:3]
    section_name = 'Suresh'
    return render(request, 'imgapp/index.html', {'section_name': section_name, 'cards': cards_query,'showall':False})


def second_page(request):
    cards_query = ImgApp.objects.all()
    return render(request, 'imgapp/index.html', {'cards': cards_query,'showall':True})

def detail_page(request, slug):
    card = ImgApp.objects.filter(slug=slug).first()  # Use filter and first to avoid exceptions
    if card:
        return render(request, 'imgapp/detail.html', {'card': card})
    else:
        return render(request, 'imgapp/404.html')  # Or a different error handling page


def About_us(request):
    return render(request, 'imgapp/AboutUs.html')

