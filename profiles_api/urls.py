from django.urls import path, include
# from profiles_api import views

from django.contrib import admin
from django.urls import path
from profiles_api.views import saludo,despedida,damefecha,calculaEdad,pokemon

urlpatterns = [
    path('saludo/',saludo),
    path('nosveremos/<str:imagen>',despedida),
    path('fecha/',damefecha),
    path('edades/<int:edad>/<int:agno>/',calculaEdad),
    path('pokemon/<str:name>/',pokemon),
]
