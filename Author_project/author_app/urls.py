from django.urls import path
from . import views

urlpatterns = [
    path('<int:details>', views.CreateProfileView.as_view(),name='post-det'),
    path('index', views.index, name='index'),
    path('postview', views.PostListView.as_view(), name='post-detail'),
    path('createview', views.CreateProfileView.as_view(),name='post-create'),
    
]