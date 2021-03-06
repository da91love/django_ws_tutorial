# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<str:room_name>/', views.room, name='room'),
    path('listener/', views.listener, name='listener')
]