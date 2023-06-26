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

    def __str__(self):
        return self.titulo

# class Tarea(models.Model):

#     ESTADO_CHOICES = (
#         ('Pendiente', 'Pendiente'),
#         ('En Progreso', 'En progreso'),
#         ('Completada', 'Completada'),
#     )
    
#     usuario = models.ForeignKey(
#         User, on_delete=models.CASCADE, null=True, blank=True)
#     titulo = models.CharField(max_length=200)
#     descripcion = models.TextField(null=True, blank=True)
#     estado = models.CharField(
#         max_length=20, choices=ESTADO_CHOICES, default='Pendiente')
#     creada = models.DateTimeField(auto_now_add=True)
#     # borrado = models.BooleanField(default=False)

#     def __str__(self):
#         return self.titulo

#     class Meta:
#         ordering = ['estado']

#     # def delete(self, *args, **kwargs):
#     #     self.borrado = True
#     #     self.save()
