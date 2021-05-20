from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.signup, name='register_user'),
    path('', views.signin, name='login_user'),
    path('logout/', views.signout, name='logout_user'),
  
]