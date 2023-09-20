from django.db import models

# Create your models here.

# Propio de usuario
class Rol(models.Model):

    idRol = models.IntegerField(primary_key=True, verbose_name="Id rol de usuario")
    nombreRol = models.CharField(max_length=10, verbose_name="nombre rol de usuario")

    def __str__(self) -> str:
        return self.nombre
    
class Usuario(models.Model):

    idUsuario = models.AutoField(primary_key=True)
    correoUsuario = models.CharField(max_length=50)
    nombreUsuario = models.CharField(max_length=50)
    passUsuario = models.CharField(max_length=50)
    rolUsuario = models.ForeignKey(Rol ,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombreUsuario
    
# Propio de producto
class Proveedor(models.Model):
    pass

class Marca(models.Model):
    pass

class Categoria(models.Model):
    pass

class Tipo_producto(models.Model):
    pass

class Producto(models.Model):
    pass

# Propio de venta
class Venta(models.Model):
    pass