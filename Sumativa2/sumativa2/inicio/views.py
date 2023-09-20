from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'inicio/index.html')  

def registro(request):
    return render(request, 'inicio/registro.html')

def recuperar(request):
    return render(request, 'inicio/recuperar.html')

def perro(request):
    count = Producto.objects.filter(categoria_producto=1).count()
    if count == 0:
        context = {
            'count' : count
        }
        return render(request, 'inicio/perro.html', context)
    else:
        productos = Producto.objects.filter(categoria_producto=1)
        context = {
            'count' : count,
            'product' : productos
        }
        return render(request, 'inicio/perro.html', context)

def gato(request):
    count = Producto.objects.filter(categoria_producto=2).count()
    if count == 0:
        context = {
            'count' : count
        }
        return render(request, 'inicio/gato.html', context)
    else:
        productos = Producto.objects.filter(categoria_producto=2)
        context = {
            'count' : count,
            'product' : productos
        }
        return render(request, 'inicio/gato.html', context)
    
def medicina(request):
    count = Producto.objects.filter(categoria_producto=3).count()
    if count == 0:
        context = {
            'count' : count
        }
        return render(request, 'inicio/medicina.html', context)
    else:
        productos = Producto.objects.filter(categoria_producto=3)
        context = {
            'count' : count,
            'product' : productos
        }
        return render(request, 'inicio/medicina.html', context)

#TODO agregar funcion para añadir a carrito desde vista de productos
def add_carrito(request):
    pass