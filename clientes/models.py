from django.db import models


class tabla(models.Model):
    nombre_cliente = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_registro = models.DateTimeField()