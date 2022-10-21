import email
from urllib import request
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import RegisterForm

from django.contrib.auth.models import User

def index (request):
    return render(request, 'login.html',{
        'message' : 'Variable del contexto',
        
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('/admin')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html',{

    })

def logout_view (request):
    logout (request)
    messages.success(request, 'Has cerrado sesion')
    return redirect('login')

def register(request):
    form = RegisterForm(request.POST or None)

    if request.method =='POST' and form.is_valid():
        username=form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')

        user=User.objects.create_superuser(username,email,password)
        if user:
            login(request, user)
            messages.success(request,'Usuario creado exitosamente')
            return redirect('login')
    return render(request,'register.html',{
        'form':form
    })