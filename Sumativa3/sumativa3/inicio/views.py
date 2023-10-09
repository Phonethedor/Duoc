from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    user_id= request.session.get('id_usuario')

    if user_id  is not None:

        usuario=Usuario.objects.get(id_usuario=user_id) 
        if usuario:
            context = {
                "usuario": usuario,
            }
            return render(request, 'inicio/index.html', context)
       
    return render(request, 'inicio/index.html')
    

def log_in(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        user = Usuario.objects.get(correo_usuario=email)
        print(user.nombre_usuario)
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario o contraseña incorrecto')
        return redirect('index')

    if user.pass_usuario == password:
        request.session['id_usuario'] = user.id_usuario
        request.session['user_name'] = user.nombre_usuario
        return redirect('index')
    else:
        messages.error(request, 'Usuario o contraseña incorrecto')

    return redirect('index')

def log_out(request):
    request.session.flush()
    return redirect('index')

def registro(request):
    return render(request, 'inicio/registro.html')

def registrar(request):
    correo = request.POST['email']
    nombre = request.POST['nombre']
    password = request.POST['pass1']

    rol = Rol.objects.get(id_rol=2)

    Usuario.objects.create(correo_usuario=correo, nombre_usuario=nombre, pass_usuario = password, rol_usuario = rol)
    messages.success(request, 'se ha registrado correctamente')
    return redirect('index')  
   
def recuperar(request):
    return render(request, 'inicio/recuperar.html') 
   
def recuperar(request):
    return render(request, 'inicio/recuperar.html')

def editar_pagina(request):
    return render(request, 'inicio/editar.html')

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
    
def stock(request):
    productos = Producto.objects.all()
    context = {
        'productos' : productos
    }
    return render(request, 'inicio/stock.html', context)

def eliminar_stock(request, id):
    producto = Producto.objects.get(id_producto=id)
    producto.delete()
    return redirect('stock')

def editar_stock(request, id):
    producto = Producto.objects.get(id_producto=id)
    context = {
        'producto' : producto
    }
    return render(request, 'inicio/editar_stock.html', context)

def modificar_stock(request):
    id = int(request.POST['id_producto'])
    stock = request.POST['stock']

    producto = Producto.objects.get(id_producto=id)
    producto.stock_producto = stock
    
    producto.save()
    return redirect('stock')

def agregar_producto(request):
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    marcas = Marca.objects.all()
    tipos = Tipo_producto.objects.all()
    context = {
        'categorias' : categorias,
        'proveedores' : proveedores,
        'marcas' : marcas,
        'tipos' : tipos
    }
    return render(request, 'inicio/agregar_producto.html', context)

def add_producto(request):
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    valor = request.POST['precio']
    stock = request.POST['stock']
    imagen = request.FILES['imagen']
    prov = request.POST['proveedor']
    proveedor = Proveedor.objects.get(id_proveedor = prov)
    marc = request.POST['marca']
    marca = Marca.objects.get(id_marca = marc)
    tip = request.POST['tipo']
    tipo = Tipo_producto.objects.get(id_tipo_producto = tip)
    categ = request.POST['categoria']
    categoria = Categoria.objects.get(id_categoria = categ)

    Producto.objects.create(
        nombre_producto=nombre, 
        descripcion_producto=descripcion, 
        valor_producto=valor, 
        stock_producto=stock,
        imagen_producto=imagen,
        proveedor_producto=proveedor,
        marca_producto=marca,
        tipo_producto=tipo,
        categoria_producto=categoria
        )
    return redirect('stock')

#TODO agregar funcion para añadir a carrito desde vista de productos
def add_carrito(request):
    pass

#TODO agregar funcion para ver carrito
def ver_carrito(request):
    pass