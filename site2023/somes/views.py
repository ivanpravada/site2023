from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify


menu = ["About", "Add article", "Feedback", "Log in"]


data_db = [
    {'id': 1, 'title': 'title_1', 'content': 'some data 1', 'is_published': True},
    {'id': 2, 'title': 'title_2', 'content': 'some data 2', 'is_published': False},
    {'id': 3, 'title': 'title_3', 'content': 'some data 3', 'is_published': True},
]


def index(request):
    data = {
        'title': 'Main page',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'somes/index.html', context=data)


def about(request):
    return render(request, 'somes/about.html', {'title': 'About'})


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