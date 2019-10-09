
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('teams', views.teams, name='teams'),
    path('about', views.about, name='about'),
]
