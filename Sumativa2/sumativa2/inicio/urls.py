from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('registro/', registro, name='registro'),
    path('log_in', log_in, name='log_in'),
    path('log_out', log_out, name='log_out'),
    path('recuperar/', recuperar, name='recuperar'),
    path('perro/', perro, name='perro'),
    path('gato/', gato, name='gato'),
    path('medicina/', medicina, name='medicina'),
]