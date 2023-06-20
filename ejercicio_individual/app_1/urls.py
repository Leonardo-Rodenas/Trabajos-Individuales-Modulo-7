from django.urls import path
from . import views
from .views import tareas_usuario
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('', views.home, name='home'),
   path('login/', views.IngresoView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'), 
   path('tareas_usuario/', tareas_usuario, name='tareas_usuario'), 
]