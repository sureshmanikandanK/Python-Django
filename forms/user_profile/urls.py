from django.urls import path
from .views import forms_page,Thanks
urlpatterns = [
    
    path('form/',forms_page,name = 'Form_page'),
    path('Thanks/',Thanks,name = 'thankyou')
]
