from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre



class Servicio(models.Model):
    ClienteId = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    fecha = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    color = models.CharField(max_length=30)


