from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
     path('', views.login1, name='login'),
     path('signup/', views.signup, name='signup'),
     path('mainpage/', views.mainpage, name='mainpage'),
     path('mediapage/<int:id>', views.mediapage, name='mediapage'),
     path('loanpage/<int:id>', views.loanpage, name='loanpage'),
     path('profile/<int:id>', views.profile, name='profile'),
     path('logout/', views.ulogout, name='logout'),


]