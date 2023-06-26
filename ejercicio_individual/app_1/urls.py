from django.urls import path
from . import views
from .views import ListaTareas, DetalleTarea, CrearTarea, ActualizarTarea, BorrarTarea, VistaLoginCustom
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('', views.home, name='home'),
   path('login/', VistaLoginCustom.as_view(), name='login'),
   path('logout/', LogoutView.as_view(next_page='login'), name='logout'), 
   path('lista_tareas/', ListaTareas.as_view(), name='lista_tareas'), 
   path('lista_tareas/<int:pk>/', DetalleTarea.as_view(), name='detalle_tarea'),
   path('crear_tarea/', CrearTarea.as_view(), name='crear_tarea'), 
   path('actualizar_tarea/<int:pk>/', ActualizarTarea.as_view(), name='actualizar_tarea'),
   path('borrar_tarea/<int:pk>/', BorrarTarea.as_view(), name='borrar_tarea'),
]