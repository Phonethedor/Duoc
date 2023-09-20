from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('registro/', registro, name='registro'),
    path('recuperar/', recuperar, name='recuperar'),
    path('perro/', perro, name='perro'),
    path('gato/', gato, name='gato'),
    path('medicina/', medicina, name='medicina'),
]