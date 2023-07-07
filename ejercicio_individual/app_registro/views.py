from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def registrar_usuario(request):
    if request.method == 'POST':
        # Obtén los datos del formulario
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        # Verifica si el usuario ya existe
        if User.objects.filter(username=username).exists():
            # Manejo de error si el usuario ya existe
            return render(request, 'registro.html', {'error': 'El nombre de usuario ya está en uso.'})

        # Verifica si el email ya existe
        if User.objects.filter(email=email).exists():
            # Manejo de error si el email ya existe
            return render(request, 'registro.html', {'error': 'El email ya está en uso.'})

        # Crea el nuevo usuario
        user = User.objects.create_user(
            username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        # Redirecciona a una página de éxito o cualquier otra página deseada
        return redirect('login')

    # Si es una solicitud GET, muestra el formulario de registro 
    return render(request, 'registro.html')
