from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'auth_demo/index.html')


def register(request):
    return render(request, 'auth_demo/register.html')


def login(request):
    return render(request, 'auth_demo/login.html')


def logout(request):
    pass
