from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DishViewset
 
router = DefaultRouter()
router.register('', DishViewset, basename='author')
app_name ='dish_app'
 
urlpatterns=[
    path('', include(router.urls)),
]