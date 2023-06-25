from typing import Any
from django.shortcuts import render
#Imports necesarios para el CRUD de tareas
from .models import Tarea #Importo modelo a usar en las vistas del CRUD
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
#Imports necesarios para el login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin #Mixim para restringuir vistas a usuarios que no esten logueados

# Create your views here.

#Renderiza Home 
def home(request):
    return render(request, 'index.html')

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
    context_object_name = 'Tareas' # Le da un nuevo nombre en el for para que no se llame simplemente object
    template_name = 'templates_app/app_1/lista_tareas.html' # modifica la ruta el template para que no sea necesario que se llame tarea_list.html (prefijo = modelo, sufijo=list, así lo busca por defecto al usar estas clases heredadas)

    #Sobreescribo el método para recibir solo las tareas del usuario logueado y no las de todos los usuario en la db
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs) #genero un contexto
        context ['Tareas'] = context ['Tareas'].filter(usuario = self.request.user) # A ese contexto le asigno las Tareas, pero filtradas de acuerdo al request.user que tengo en la plantilla de lista_tareas.html
        context ['count'] = context ['Tareas'].filter(estado = True).count # Esto es para contar las tareas incompletas
        #Entrada de valores y configuración de la búsqueda
        input_busqueda = self.request.GET.get('search-area') or '' #Esto indica que la busqueda puede tener un valor o dejarse ne blanco ('')
        if input_busqueda:
            context ['Tareas'] = context ['Tareas'].filter(titulo__icontains = input_busqueda) # Acá busca por título
        
        context ['input_busqueda'] = input_busqueda      
        return context

#Ver Detalle Tareas
class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea # Modelo a utilizar
    context_object_name = 'Tarea' # Le da un nuevo nombre en el for para que no se llame simplemente object
    template_name = 'templates_app/app_1/detalle_tarea.html' # modifica la ruta el template para que no sea necesario que se llame tarea_detail.html (prefijo = modelo, sufijo=detail, así lo busca por defecto al usar estas clases heredadas)

#Crear Tareas
class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea # Modelo a utilizar
    fields = ['titulo', 'descripcion', 'estado'] # Crea los campos para el formulario a partir del modelo
    success_url = reverse_lazy('lista_tareas') # Al tener exito al crear la tarea redirigir a lista_tareas
     
     #Sobreescribo este método para hacer que las tareas creadas sean agregadas al usuario que está logueado y no al primer usuario en la db
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CrearTarea, self).form_valid(form)

#Actualizar Tareas
class ActualizarTarea(LoginRequiredMixin, UpdateView):
     model = Tarea # Modelo a utilizar
     fields = ['titulo', 'descripcion', 'estado'] # Crea todos los campos para el formulario a partir del modelo
     success_url = reverse_lazy('lista_tareas') # Al tener exito al actualizar la tarea redirigir a lista_tareas

#Borrar Tareas
class BorrarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea # Modelo a utilizar
    context_object_name = 'Tareas' # Le da un nuevo nombre en el for para que no se llame simplemente object
    success_url = reverse_lazy('lista_tareas') # Al tener exito al borrar la tarea redirigir a lista_tareas