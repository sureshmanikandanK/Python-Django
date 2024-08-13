from django.urls import path
from .import views

urlpatterns = [
    path('index',views.index),
    path('<int:month>',views.monthly_details_by_number),
    path('<str:month>',views.montly_details,name='rend_app'),

    # path('jan',views.jan),
    # path('New',views.feb),
]