from django.contrib import admin
from .models import *
# Register your models here.
# cree un superuser  user:admin  pass:1234 
# admin@duocuc.cl

admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Proveedor)
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Tipo_producto)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Detalle_venta)