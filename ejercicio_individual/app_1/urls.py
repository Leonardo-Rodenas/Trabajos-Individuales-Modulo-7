from django.urls import path
from . import views
from .views import IngresoView, tareas_usuario
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('', views.home, name='home'),
   path('login/', IngresoView.as_view(), name='login'),
   path('logout/', LogoutView.as_view(next_page='login'), name='logout'), 
   path('lista_tareas/', tareas_usuario, name='lista_tareas'), 
]