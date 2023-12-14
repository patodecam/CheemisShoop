import datetime
from django.db import models
from tabnanny import verbose
from distutils.command.upload import upload
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de Categoria")
    nombreCategoria= models.CharField(max_length=50, blank=True, verbose_name="Nombre de Categoria")
    
    def __str__(self):
        return self.nombreCategoria 
    
class Producto(models.Model):
    codigo= models.CharField(primary_key=True, max_length=8, verbose_name="Codigo Producto")
    nombre=models.CharField(max_length=50, blank=True, verbose_name="Nombre Producto")
    descripcion=models.TextField(max_length=200, blank=True, verbose_name="Descripcion del Producto")
    precios=models.IntegerField( blank=True, verbose_name="Precio del producto")
    stock=models.IntegerField( blank=True, verbose_name="Cantidad de producto en inventario")
    imagen=models.ImageField(upload_to='imagenes', null=True ,verbose_name="Imagen")
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    
    def __str__(self):
        return self.nombre

#Clase de las boletas y detalle boletas 
class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    envio=models.BigIntegerField()
    impuestos=models.BigIntegerField()
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
    usuario=models.CharField(max_length=50, blank=True, verbose_name="Usuario")
    estado=models.TextField(max_length=200, blank=True, verbose_name="Estado de la compra")
    
    def __str__(self):
        return str(self.id_boleta)

class Detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)