from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import redirect
from django.urls import reverse


def index(request):
    return HttpResponse("Somes site")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Categories by id</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Categories by slug</h1><p>id: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('music', ))
        return HttpResponsePermanentRedirect(uri)
    return HttpResponse(f"<h1>Archive by year</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")