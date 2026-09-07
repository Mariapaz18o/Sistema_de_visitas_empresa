from django.db import models

class Visita(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)  # ej: 12.345.678-5
    motivo = models.CharField(max_length=200)
    hora_entrada = models.DateTimeField(auto_now_add=True)  # se llena solo al crear
    hora_salida = models.DateTimeField(null=True, blank=True)  # se llena después, al salir

    def __str__(self):
        return f"{self.nombre} - {self.rut}"