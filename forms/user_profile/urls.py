from django.urls import path
from .views import forms_page 
urlpatterns = [
    
    path('form/',forms_page),
]
