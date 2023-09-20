from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'inicio/index.html')  

def registro(request):
    return render(request, 'inicio/registro.html')

def recuperar(request):
    return render(request, 'inicio/recuperar.html')

#TODO agregar funcion para contar productos con la categoria en cuestion y enviar a template
def perro(request):
    return render(request, 'inicio/perro.html')

#TODO agregar funcion para contar productos con la categoria en cuestion y enviar a template
def gato(request):
    return render(request, 'inicio/gato.html')

#TODO agregar funcion para contar productos con la categoria en cuestion y enviar a template
def medicina(request):
    return render(request, 'inicio/medicina.html')

#TODO agregar funcion para añadir a carrito desde vista de productos
def add_carrito(request):
    pass