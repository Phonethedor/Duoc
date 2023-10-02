from rest_framework import serializers
from inicio.models import Producto

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            'id_producto',
            'nombre_producto', 
            'descripcion_producto',
            'valor_producto',
            'stock_producto']