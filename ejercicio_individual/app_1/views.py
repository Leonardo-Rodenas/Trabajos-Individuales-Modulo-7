from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import Tarea
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

#Renderiza Home 
def home(request):
    return render(request, 'index.html')

#Renderiza el Login
class IngresoView(TemplateView):
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('lista_tareas')
            form.add_error('username', 'Credenciales incorrectas')
            return render(request, self.template_name, {"form": form})
        else:
            return render(request, self.template_name, {"form": form})

#Renderiza Logout
@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

#Renderiza Tareas
class ListaTareas(ListView):
    model = Tarea # Modelo a utilizar
    context_object_name = 'Tareas' # Le da un nuevo nombre en el for para que no se llame simplemente object
    template_name = 'templates_app/app_1/lista_tareas.html' # modifica la ruta el template para que no sea necesario que se llame tarea_list.html (prefijo = modelo, sufijo=list, así lo busca por defecto al usar estas clases heredadas)

class DetalleTarea(DetailView):
    model = Tarea # Modelo a utilizar
    context_object_name = 'Tarea' # Le da un nuevo nombre en el for para que no se llame simplemente object
    template_name = 'templates_app/app_1/detalle_tarea.html' # modifica la ruta el template para que no sea necesario que se llame tarea_detail.html (prefijo = modelo, sufijo=detail, así lo busca por defecto al usar estas clases heredadas)

class CrearTarea(CreateView):
     model = Tarea # Modelo a utilizar
     fields = '__all__' # Crea todos los campos para el formulario a partir del modelo
     success_url = reverse_lazy('lista_tareas') # Al tener exito al crear la tarea redirigir a lista_tareas

class ActualizarTarea(UpdateView):
     model = Tarea # Modelo a utilizar
     fields = '__all__' # Crea todos los campos para el formulario a partir del modelo
     success_url = reverse_lazy('lista_tareas') # Al tener exito al actualizar la tarea redirigir a lista_tareas

class BorrarTarea(DeleteView):
    model = Tarea # Modelo a utilizar
    context_object_name = 'Tareas' # Le da un nuevo nombre en el for para que no se llame simplemente object
    success_url = reverse_lazy('lista_tareas') # Al tener exito al borrar la tarea redirigir a lista_tareas