from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from worker.models import Place


def index(request):
    if request.user.is_authenticated:
        places = Place.objects.all()
        context = {"Places": places}
        return render(request, 'index.html', context)
    return redirect('/login')


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            return render(request, 'login.html')

    return render(request, 'login.html')


def log_out(request):
    logout(request)
    return redirect('/login')
