from django.contrib import admin
from django.urls import path
from .views import HomeView, weather_view



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('weather/', weather_view, name='weather_view'),
   
]