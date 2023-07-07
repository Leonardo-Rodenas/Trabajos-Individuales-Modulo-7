from django import forms
from .models import Tarea
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', required=True,
                               max_length=50, min_length=2,
                               error_messages={
                                   'required': 'El usuario es obligatorio',
                                   'max_length': 'El usuario no puede superar los 50 caracteres',
                                   'min_length': 'El usuario debe tener al menos 2 caracteres'
                               },
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Ingrese su usuario',
                                   'class': 'form-control'
                               })
                               )
    password = forms.CharField(label='Contraseña', required=True,
                               max_length=50, min_length=1,
                               error_messages={
                                   'required': 'La contraseña es obligatoria',
                                   'max_length': 'La contraseña no puede superar los 50 caracteres',
                                   'min_length': 'La contraseña debe tener al menos 1 caracter'
                               },
                               widget=forms.PasswordInput(attrs={
                                   'placeholder': 'Ingrese su contraseña',
                                   'class': 'form-control'
                               })
                               )
        
class TareaForm(forms.ModelForm):
    destinatario = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'estado', 'fecha_vencimiento', 'etiqueta', 'prioridad', 'destinatario']
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'})
        }

class ObservacionForm(forms.Form):
    observaciones = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}) 
    )