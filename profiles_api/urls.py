from django.urls import path, include
# from profiles_api import views

from django.contrib import admin
from django.urls import path
from profiles_api.views import saludo,pokemon

urlpatterns = [
    path('saludo/',saludo), 
    path('pokemon/<str:name>/',pokemon),
]

