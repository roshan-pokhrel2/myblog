from django.urls import path
from .import views



urlpatterns = [
    path('', views.home, name= 'home'),
    path('register', views.register, name='register'),
    path('addblog', views.blogpost, name='addblog'),
    path('blog', views.blog, name='blog'),
    path('login', views.logging, name='login'),
    path('logout', views.loggingout, name='logout'),
    path('details/<int:pk>', views.details, name='readmore'),
    path('profile', views.profilefun, name='profile'),
] 
