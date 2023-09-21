from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def index(request):
    if 'id_usuario' not in request.session:
        return render(request, 'inicio/index.html')
        
    context = {
        "usuario": Usuario.objects.get(id_usuario=request.session['id']),
    }
    return render(request, 'inicio/index.html', context)

def log_in(request):
    user = Usuario.objects.filter(correo_usuario=request.POST['email'].lower())
    password = Usuario.objects.filter(pass_usuario=request.POST['password'].lower())

    if len(user != password):        
        return redirect('/')
    else:
        request.session['id'] = user[0].id_usuario
        request.session['user_name'] = user[0].nombre_usuario
        return redirect('/')  
    
def log_out(request):
    request.session.flush()
    return redirect('/')

def registro(request):
    return render(request, 'inicio/registro.html')

def recuperar(request):
    return render(request, 'inicio/recuperar.html')

@login_required(login_url='inicio/index.html')
def editar(request):
    id = int(request.POST['id'])
    email = request.POST['email']
    nombre = request.POST['nombre']
    password = request.POST['pass1']

    user = Usuario.objects.get(id_usuario=id)
    user.correo_usuario = email
    user.nombre_usuario = nombre
    user.pass_usuario = password
    user.save()
    return redirect('/')

@login_required(login_url='inicio/index.html')
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

@login_required(login_url='inicio/index.html')
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

@login_required(login_url='inicio/index.html')
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