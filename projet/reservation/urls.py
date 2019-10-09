
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('reservation', views.reservation, name='reservation'),
]
