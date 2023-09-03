from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Somes site")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Categories by id</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Categories by slug</h1><p>id: {cat_slug}</p>")


def archive(request, year):
    return HttpResponse(f"<h1>Archive by year</h1><p>{year}</p>")