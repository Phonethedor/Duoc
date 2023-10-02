from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from inicio.models import Producto
from .serializers import *

# Create your views here.
@csrf_exempt
@api_view(['GET'])
def lista_productos(request):
    pass
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializers(producto, many = True)
        return Response(serializer.data)
    else:
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)