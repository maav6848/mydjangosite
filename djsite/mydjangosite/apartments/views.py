from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<H1> Главная страница приложения <H1/>")


