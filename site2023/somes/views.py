from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Somes site")


def categories(request):
    return HttpResponse("<h1>Categories</h1>")