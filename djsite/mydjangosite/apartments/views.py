from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<H1> Главная страница приложения </H1>")

def catigories(request):
    return HttpResponse("Категории")

#def rent(response):
#    return HttpResponse("Аренда квартир")

#def delivery(response):
 #   return HttpResponse("Сдача квартир в аренду")