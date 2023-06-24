from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import Tarea
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
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
                    return redirect('tareas_usuario')
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
    model = Tarea
    context_object_name = 'Tareas'
    template_name = 'templates_app/app_1/lista_tareas.html'

class DetalleTarea(DetailView):
    model = Tarea
    context_object_name = 'Tarea'
    template_name = 'templates_app/app_1/detalle_tarea.html'

class CrearTarea(CreateView):
     model = Tarea
     field = '__all__' # Crea todos los campos para el formulario a partir del modelo
     success_url = reverse_lazy('lista_tareas') # Al tener exito al crear la tarea redirigir a lista_tareas
     