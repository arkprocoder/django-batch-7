from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('blog',views.handleBlog,name='handleBlog'),
    path('services',views.services,name='services'),
    path('signup',views.signup,name='signup'),
    path('login',views.handlelogin,name='handlelogin'),
    path('logout',views.handlelogout,name='handlelogout')
   
]