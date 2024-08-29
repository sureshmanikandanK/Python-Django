from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewset
 
router = DefaultRouter()
router.register('', CategoryViewset, basename='category')
app_name ='category_app'
 
urlpatterns=[
    path('', include(router.urls)),
]