from django.urls import path
from . import views
from .views import VistaLoginCustom, ListaTareas, DetalleTarea
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('', views.home, name='home'),
   path('login/', VistaLoginCustom.as_view(), name='login'),
   path('logout/', LogoutView.as_view(next_page='login'), name='logout'), 
   path('lista_tareas/', ListaTareas.as_view(), name='lista_tareas'), 
   path('lista_tareas/tarea_n_<int:pk>/', DetalleTarea.as_view(), name='detalle_tarea'), 
]