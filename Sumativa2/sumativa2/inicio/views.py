from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'inicio/index.html')  

def registro(request):
    return render(request, 'inicio/registro.html')

def recuperar(request):
    return render(request, 'inicio/recuperar.html')