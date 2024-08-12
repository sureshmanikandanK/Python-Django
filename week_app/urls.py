from django.urls import path # type: ignore
from .import views

urlpatterns = [
    path('<int:day>',views.week),
    path('<str:day>',views.week_display,name='Days'),

    # path('jan',views.jan),
    # path('New',views.feb),
]