from django.urls import path
from .import views

urlpatterns = [
    path('<int:month>',views.monthly_details_by_number),
    path('<str:month>',views.montly_details,name='myapp'),

    # path('jan',views.jan),
    # path('New',views.feb),
]