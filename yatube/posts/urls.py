# first_programm/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница сообщества groups
    path('group/<slug:slug>/', views.group_posts),
    
]