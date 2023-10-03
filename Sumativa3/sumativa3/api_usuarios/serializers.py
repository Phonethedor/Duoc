from rest_framework import serializers
from inicio.models import Usuario

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id_usuario',
            'nombre_usuario',
            'correo_usuario',
            'created_at']