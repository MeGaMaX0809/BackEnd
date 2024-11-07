from django.db import models

class Luchador(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)  # Cambia a minúsculas
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.FloatField()
    nacionalidad = models.CharField(max_length=50)
    record = models.CharField(max_length=10, default='0-0-0')
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)

    def __str__(self):
        return self.nombre

    def clean(self):
        # Validaciones personalizadas
        if self.peso <= 0:
            raise ValueError('El peso debe ser un número positivo.')
        if self.altura <= 0:
            raise ValueError('La altura debe ser un número positivo.')
        
        partes = self.record.split('-')  # Cambié '_' por '-' para que coincida con tu formato
        if len(partes) != 3 or not all(part.isdigit() for part in partes):
            raise ValueError('El record debe ingresarse como "Victorias-Derrotas-Empates".')
