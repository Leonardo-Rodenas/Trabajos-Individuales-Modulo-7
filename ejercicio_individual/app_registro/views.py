from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def registrar_usuario(request):
    grupos = Group.objects.all()  # Obtén todos los grupos de usuarios

    if request.method == 'POST':
        # Obtén los datos del formulario
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        grupo_id = request.POST.get('grupo', None)

        # Verifica si el usuario ya existe
        if User.objects.filter(username=username).exists():
            # Manejo de error si el usuario ya existe
            return render(request, 'registro.html', {'error': 'El nombre de usuario ya está en uso.', 'grupos': grupos})

        # Verifica si el email ya existe
        if User.objects.filter(username=username).exists():
            # Manejo de error si el email ya existe
            return render(request, 'registro.html', {'error': 'El email ya está en uso.', 'grupos': grupos})

        # Crea el nuevo usuario
        user = User.objects.create_user(
            username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        # Verifica si se seleccionó un grupo
        if grupo_id:
            grupo = Group.objects.get(id=grupo_id)
            user.groups.add(grupo)

        # Redirecciona a una página de éxito o cualquier otra página deseada
        return redirect('registro')

    # Si es una solicitud GET, muestra el formulario de registro con el select de grupos
    return render(request, 'registro.html', {'grupos': grupos})
