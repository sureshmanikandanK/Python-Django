from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewset
 
router = DefaultRouter()
router.register('', BookViewset, basename='Book')
app_name ='book_app'
 
urlpatterns=[
    path('', include(router.urls)),
]