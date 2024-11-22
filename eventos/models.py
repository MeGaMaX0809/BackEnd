from django.db import models
from Eva_2.models import Luchador  # Relación con Luchador

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField()
    lugar = models.CharField(max_length=200, default="Lugar Desconocido")
    imagen = models.ImageField(upload_to='eventos/', blank=True, null=True)
    luchadores = models.ManyToManyField(Luchador, blank=True)

    def __str__(self):
        return self.nombre
