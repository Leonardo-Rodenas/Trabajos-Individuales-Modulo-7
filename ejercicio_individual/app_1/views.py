from typing import Any
from django.shortcuts import render
#Imports necesarios para el CRUD de tareas
from .models import Tarea #Importo modelo a usar en las vistas del CRUD
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.urls import reverse_lazy
#Imports necesarios para el login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin #Mixim para restringuir vistas a usuarios que no esten logueados

# Create your views here.

#Renderiza Home 
def home(request):
    return render(request, 'index.html')

#Clase para hacer el nuevo Login
class VistaLoginCustom(LoginView):
    template_name = 'registration/login.html'
    fields = '__all__' # Crea todos los campos para el formulario a partir del modelo
    redirect_authenticated_user = True # Rediderciona si el login es exitoso
    
    def get_success_url(self):
        return reverse_lazy('lista_tareas') # Lugar al que se es redirecionado si el login es exitoso

#Renderiza Tareas

#Ver lista Tareas
class ListaTareas(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = 'Tareas'
    template_name = 'templates_app/app_1/lista_tareas.html'
    ordering = ['fecha_vencimiento']

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(usuario=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tareas_usuario = self.get_queryset()
        context['Tareas'] = tareas_usuario
        context['count'] = tareas_usuario.filter(estado='Pendiente').count()
        return context
  
#Ver Detalle Tareas
class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea # Modelo a utilizar
    context_object_name = 'Tarea' # Le da un nuevo nombre en el for para que no se llame simplemente object
    template_name = 'templates_app/app_1/detalle_tarea.html' # modifica la ruta el template para que no sea necesario que se llame tarea_detail.html (prefijo = modelo, sufijo=detail, así lo busca por defecto al usar estas clases heredadas)