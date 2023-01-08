from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Todo
# Create your views here.


@login_required
def index(request):
    if request.method == 'POST':
        text = request.POST.get("text").strip()
        if text:
            Todo.objects.create(text=text, user=request.user)
        return redirect('/')
    todos = Todo.objects.filter(user=request.user)
    context = {
        'todos': todos,
    }
    return render(request, 'todoapp/index.html', context)


@login_required
def deleteTodo(request, id):
    get_object_or_404(Todo, id=id, user=request.user).delete()
    return redirect("/")


def about(request):
    return render(request, 'todoapp/about.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            authLogin(request, user)
            messages.add_message(request, messages.SUCCESS,
                                 "Successfully Logged In")
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, "Wrong Credentials")
            return redirect('login')

    return render(request, 'todoapp/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if password != confirmPassword:
            messages.add_message(request, messages.ERROR, "Both password should be same")
            return redirect('register')
        
        create_user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        if create_user:
            user = authenticate(username=username, password=password)
            if user is not None:
                authLogin(request, user)
                messages.add_message(request, messages.SUCCESS, "Registration Successfull")
                return redirect('index')

    return render(request, 'todoapp/register.html')


@login_required
def logout(request):
    authLogout(request)
    return redirect('login')
