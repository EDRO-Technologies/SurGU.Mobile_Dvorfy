from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')


def registration(request):
    return render(request, 'register.html')

def auth(request):
    return render(request, 'Auth.html')


