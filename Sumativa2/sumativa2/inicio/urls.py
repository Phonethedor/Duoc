from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('registro/', registro, name='registro'),
    path('recuperar/', recuperar, name='recuperar'),
]