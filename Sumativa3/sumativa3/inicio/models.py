from django.db import models

# Create your models here.

# Propio de usuario

# Rol usuario (1 = admin, 2 = cliente)
class Rol(models.Model):

    id_rol = models.IntegerField(primary_key=True, verbose_name="Id rol de usuario")
    nombre_rol = models.CharField(max_length=10, verbose_name="nombre rol de usuario")

    def __str__(self) -> str:
        return self.nombre_rol
    
# Tabla usuario
class Usuario(models.Model): 

    id_usuario = models.AutoField(primary_key=True)
    correo_usuario = models.CharField(unique=True, max_length=50)
    nombre_usuario = models.CharField(unique=True, max_length=50)
    pass_usuario = models.CharField(max_length=50)
    rol_usuario = models.ForeignKey(Rol ,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre_usuario
    
# Propio de producto

# Quien nos vende los productos
class Proveedor(models.Model):
    
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre_proveedor

# Manufacturador de producto
class Marca(models.Model):
    
    id_marca = models.AutoField(primary_key=True)
    nombre_marca = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre_marca

# categoria producto (gato, perro, medicina)
class Categoria(models.Model):

    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre_categoria

# Tipo de producto (alimento, medicamento) (para futura implementacion de funcion de filtrado)
class Tipo_producto(models.Model):
    
    id_tipo_producto = models.AutoField(primary_key=True)
    descripcion_tipo_producto = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.descripcion_tipo_producto

# Producto en cuestion (created_at es la fecha que fue creado el registro y updated_at es la fecha en que se modifica)
class Producto(models.Model):
    
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=50)
    descripcion_producto = models.CharField(max_length=200)
    valor_producto = models.IntegerField()
    stock_producto = models.IntegerField()
    imagen_producto = models.ImageField(upload_to="imagenes")
    proveedor_producto = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    marca_producto = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria_producto = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tipo_producto = models.ForeignKey(Tipo_producto, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre_producto

# Propio de venta

# Tabla que registra los movimientos individuales de productos para luego ser incorporados en el detalle
class Venta(models.Model):
    
    id_venta = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.IntegerField()

# Contiene la cantidad total de la venta y tambien la fecha en que se realizo
class Detalle_venta(models.Model):
    
    id_detalle = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ventas = models.ForeignKey(Venta, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)