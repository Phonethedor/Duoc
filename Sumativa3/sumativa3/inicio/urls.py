from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('registro/', registro, name='registro'),
    path('registrar', registrar, name='registrar'),
    path('log_in/', log_in, name='log_in'),
    path('log_out/', log_out, name='log_out'),
    path('recuperar/', recuperar, name='recuperar'),
    path('edit/', editar_pagina, name='editar_pagina'),
    path('editar/', editar, name='editar'),
    path('stock/', stock, name='stock'),
    path('eliminar_stock/<int:id>', eliminar_stock, name='eliminar_stock'),
    path('editar_stock/<int:id>', editar_stock, name='editar_stock'),
    path('modificar_stock/', modificar_stock, name='modificar_stock'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('add_producto', add_producto, name="add_producto"),
    path('perro/', perro, name='perro'),
    path('gato/', gato, name='gato'),
    path('medicina/', medicina, name='medicina'),
]