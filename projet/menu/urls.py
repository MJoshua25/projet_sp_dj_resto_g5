
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('specialSalmon', views.special, name='specialSalmon'),
    #path('/specialBeaf', views.special, name='specialBeaf'),
]
