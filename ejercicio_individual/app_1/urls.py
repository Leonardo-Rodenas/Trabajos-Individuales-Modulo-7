from django.urls import path
from . import views
from .views import VistaLoginCustom, ListaTareas, DetalleTarea, CrearTarea, ActualizarTarea, BorrarTarea
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('', views.home, name='home'),
   path('login/', VistaLoginCustom.as_view(), name='login'),
   path('logout/', LogoutView.as_view(next_page='login'), name='logout'), 
   path('lista_tareas/', ListaTareas.as_view(), name='lista_tareas'), 
   path('lista_tareas/tarea_n_<int:pk>/', DetalleTarea.as_view(), name='detalle_tarea'), 
   path('crear_tarea/', CrearTarea.as_view(), name='crear_tarea'),
   path('actualiza_tarea/tarea_n_<int:pk>/', ActualizarTarea.as_view(), name='actualiza_tarea'), 
   path('borrar_tarea/tarea_n_<int:pk>/', BorrarTarea.as_view(), name='borrar_tarea'),
   # path('completar-tarea/<int:tarea_id>/', completar_tarea, name='completar_tarea'),
]