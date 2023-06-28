from django.db import models
from django.contrib.auth.models import User

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):

    ESTADO_CHOICES = (
        ('Pendiente', 'Pendiente'),
        ('En Progreso', 'En progreso'),
        ('Completada', 'Completada'),
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_vencimiento = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')
    etiqueta = models.ManyToManyField(Etiqueta, related_name='tareas')
    observaciones = models.TextField(blank=True, null=True) # Nuevo atributo solicitado en el trabajo individual

    def __str__(self):
        return self.titulo