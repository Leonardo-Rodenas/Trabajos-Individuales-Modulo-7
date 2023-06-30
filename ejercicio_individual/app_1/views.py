from django.shortcuts import render
#Imports necesarios para el CRUD de tareas
from .models import Tarea, Etiqueta #Importo modelo a usar en las vistas del CRUD
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import TareaForm
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
    model = Tarea # Modelo a utilizar
    context_object_name = 'Tareas'  # Le da un nuevo nombre en el for para que no se llame simplemente object
    template_name = 'templates_app/app_1/lista_tareas.html' # modifica la ruta el template para que no sea necesario que se llame tarea_detail.html (prefijo = modelo, sufijo=list, así lo busca por defecto al usar estas clases heredadas)
    ordering = ['-fecha_vencimiento'] # Ordena por fecha vencimiento

    def get_queryset(self): # Acá ordeno las querys para ordenar las tareas 
        queryset = super().get_queryset()
        queryset = queryset.filter(usuario=self.request.user)
        return queryset

    def get_context_data(self, **kwargs): # Recibe las tareas sólo del usuario logueado y no todas las tareas en la base de datos.
        context = super().get_context_data(**kwargs)
        tareas_usuario = self.get_queryset()
        context['Tareas'] = tareas_usuario # Tareas de una persona
        context['count'] = tareas_usuario.filter(estado='Pendiente').count() # Cuenta las tareas pendientes
        etiquetas = Etiqueta.objects.all()  # Obtener todas las etiquetas
        context['etiquetas'] = etiquetas  # Agregar las etiquetas al contexto
        return context
  
#Ver Detalle Tareas
class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea # Modelo a utilizar
    context_object_name = 'Tarea' # Le da un nuevo nombre en el for para que no se llame simplemente object
    template_name = 'templates_app/app_1/detalle_tarea.html' # modifica la ruta el template para que no sea necesario que se llame tarea_detail.html (prefijo = modelo, sufijo=detail, así lo busca por defecto al usar estas clases heredadas)
  
#Crear Tareas
class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'templates_app/app_1/crea_actualiza_tarea.html' # modifica la ruta el template para que no sea necesario que se llame tarea_detail.html (prefijo = modelo, sufijo=detail, así lo busca por defecto al usar estas clases heredadas)
    success_url = reverse_lazy('lista_tareas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        etiquetas = Etiqueta.objects.all()  # Obtener todas las etiquetas
        context['etiquetas'] = etiquetas  # Agregar las etiquetas al contexto
        estados = Tarea.estado  # Obtener todos los estados del modelo Tarea
        context['estados'] = estados  # Agregar los estados al contexto
        return context