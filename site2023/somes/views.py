from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string


menu = ["About", "Add article", "Feedback", "Log in"]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def index(request):
    # t = render_to_string('somes/index.html')
    # return HttpResponse(t)
    data = {
        'title': 'Main page',
        'menu': menu,
        'float': 22.34,
        'lst': [1, 2, 'ab', True],
        'set': {2, 5, 'mm'},
        'dict': {'key1': 'value2', 'key2': 'value2'},
        'obj': MyClass(10, 20)
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