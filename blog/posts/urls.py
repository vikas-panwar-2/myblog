from . import views
from django.urls import path

urlpatterns = [
    path('list/', views.PostList, name='home'),
    path('create/', views.PostCreate, name='post_create'),
    path('detail/<post_id>/', views.PostDetail, name='post_detail'),
]