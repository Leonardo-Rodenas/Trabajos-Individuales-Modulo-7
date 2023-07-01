from django.shortcuts import render, get_object_or_404
#Imports necesarios para el CRUD de tareas
from .models import Tarea, Etiqueta #Importo modelo a usar en las vistas del CRUD
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
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
    ordering = ['-fecha_creacion'] # Ordena por fecha creación (más nueva arriba, más antigua abajo)

    def get_queryset(self): # Acá ordeno las querys para ordenar las tareas y filtrar para obtener sólo las tareas del usuario logueado
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
        # Hacer el filtro del select
        if self.request.GET.get('filtro') == 'buscar':
            input_busqueda = self.request.GET.get('search-area') or '' #Esto indica que la busqueda puede tener un valor o dejarse ne blanco ('')
            if input_busqueda:
                context ['Tareas'] = context ['Tareas'].filter(titulo__icontains = input_busqueda) # Acá busca por título
            context['input_busqueda'] = input_busqueda 
        # if self.request.GET.get('filtro') == 'filtrar':
        #     input_busqueda = self.request.GET.get('etiqueta') or '' #Esto indica que la busqueda puede tener un valor o dejarse ne blanco ('')
        #     if input_busqueda:
        #         context ['Tareas'] = context ['Tareas'].filter(titulo__icontains = input_busqueda) # Acá busca por título
        #     context['input_busqueda'] = input_busqueda 
        return context
  
#Ver Detalle Tareas
class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea # Modelo a utilizar
    context_object_name = 'Tarea' # Le da un nuevo nombre en el for para que no se llame simplemente object
    template_name = 'templates_app/app_1/detalle_tarea.html' # modifica la ruta el template para que no sea necesario que se llame tarea_detail.html (prefijo = modelo, sufijo=detail, así lo busca por defecto al usar estas clases heredadas)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     tarea = self.object  # Get the Tarea object
    #     context['form_initial'] = {
    #         'titulo': tarea.titulo,
    #         'descripcion': tarea.descripcion,
    #         'fecha_vencimiento': tarea.fecha_vencimiento,
    #         'estado': tarea.estado,
    #         'etiqueta': tarea.etiqueta
    #     }
    #     return context

#Crear Tareas
class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea # Modelo a utilizar
    form_class = TareaForm # Formulario a utilizar para crear la tarea
    template_name = 'templates_app/app_1/crea_actualiza_tarea.html' # modifica la ruta el template para que no sea necesario que se llame tarea_detail.html (prefijo = modelo, sufijo=form, así lo busca por defecto al usar estas clases heredadas)
    success_url = reverse_lazy('lista_tareas') # Si la tarea se crea de forma exitosa, volver al listado de tareas

    def form_valid(self, form):
        form.instance.usuario = self.request.user # Generar instancia del formulario y si es válido, etonces se puede crear la tarea, de lo contrario si falta algo no se creará
        return super().form_valid(form)    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Obtener el contexto
        etiquetas = Etiqueta.objects.all()  # Obtener todas las etiquetas
        context['etiquetas'] = etiquetas  # Agregar las etiquetas al contexto
        estados = Tarea.estado  # Obtener todos los estados del modelo Tarea
        context['estados'] = estados  # Agregar los estados al contexto
        return context
    
#Actualizar Tareas   
class ActualizarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea # Modelo a utilizar
    form_class = TareaForm # Formulario a utilizar para actualizar la tarea
    template_name = 'templates_app/app_1/crea_actualiza_tarea.html' # modifica la ruta el template para que no sea necesario que se llame tarea_detail.html (prefijo = modelo, sufijo=form, así lo busca por defecto al usar estas clases heredadas)
     
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs) # Obtener el contexto
       etiquetas = Etiqueta.objects.all()  # Obtener todas las etiquetas
       context['etiquetas'] = etiquetas  # Agregar las etiquetas al contexto
       estados = Tarea.estado  # Obtener todos los estados del modelo Tarea
       context['estados'] = estados  # Agregar los estados al contexto
       return context
    
    # def get_initial(self):
    #     initial = super().get_initial()
    #     form_initial = self.kwargs.get('form_initial')
    #     if form_initial:
    #         initial.update(form_initial)
    #     return initial
    
    def get_success_url(self):
       return reverse_lazy('detalle_tarea', kwargs={'pk': self.object.pk}) # Al tener exito al actualizar la tarea redirigir a detalle_tarea
   
        
        
       


        
    