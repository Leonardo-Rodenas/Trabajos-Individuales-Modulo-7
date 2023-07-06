from django.contrib import admin
from .models import Tarea, Etiqueta, Prioridad

# Register your models here.

admin.site.register(Tarea)
admin.site.register(Etiqueta)
admin.site.register(Prioridad)