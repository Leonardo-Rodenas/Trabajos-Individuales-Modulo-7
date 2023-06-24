from django.db import models
from django.contrib.auth.models import User

class TareaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(borrado=False)

# class Etiqueta(models.Model):
#     ETIQUETA_CHOICES = (
#         ('Trabajo', 'Trabajo'),
#         ('Hogar', 'Hogar'),
#         ('Estudio', 'Estudio'),
#         ('Deporte', 'Deporte'),
#         ('Personal', 'Personal'),
#         ('Entretención', 'Entretención'),
#         ('Otro', 'Otro')
#     )
    
#     id = models.AutoField(primary_key=True)    
#     nombre = models.CharField(max_length=20, choices=ETIQUETA_CHOICES, default='Otro')
#     borrado = models.BooleanField(default=False)

#     def __str__(self):
#         return self.nombre
    
#     def delete(self, *args, **kwargs):
#         self.borrado = True
#         self.save()

# class Tarea(models.Model):
ESTADO_CHOICES = (
    ('Pendiente', 'Pendiente'),
    ('En Progreso', 'En progreso'),
    ('Completada', 'Completada'),
)

#     id = models.AutoField(primary_key=True)
#     usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#     titulo = models.CharField(max_length=100)
#     descripcion = models.TextField()
#     fecha_vencimiento = models.DateField()
#     estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')
#     etiqueta = models.OneToOneField(Etiqueta, on_delete=models.CASCADE, related_name='tarea')  # Relación uno a uno
#     borrado = models.BooleanField(default=False)

#     objects = TareaManager()  # Usamos el manager personalizado

#     def __str__(self):
#         return self.titulo

#     def delete(self, *args, **kwargs):
#         self.borrado = True
#         self.save()

class Tarea(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')
    creada = models.DateTimeField(auto_now_add=True)
    borrado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['estado']

    def delete(self, *args, **kwargs):
        self.borrado = True
        self.save()