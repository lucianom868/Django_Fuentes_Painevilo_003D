from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(primary_key = True, max_length = 9, verbose_name = 'Rut')
    nombre = models.CharField(max_length = 50, verbose_name = 'Nombre')
    email = models.CharField(max_length= 50, verbose_name='Email', null=True)
    
    def __str__(self):
        return self.rut


class Producto(models.Model):
    codigo = models.CharField(primary_key = True, max_length = 10, verbose_name = 'Codigo')
    nombre = models.CharField(max_length = 50, verbose_name = 'Nombre')
    descripcion = models.CharField(max_length = 200, verbose_name = 'Descripcion')
    precio = models.IntegerField(verbose_name='Precio')
    imagen = models.ImageField(upload_to="imagenes", null=True)
        
    def __str__(self):
        return self.codigo 