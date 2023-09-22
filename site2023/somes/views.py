from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render


menu = [
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Add article', 'url_name': 'addpage'},
    {'title': 'Feedback', 'url_name': 'contact'},
    {'title': 'Log in', 'url_name': 'login'},
]


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
    return render(request, 'somes/about.html', {'title': 'About', 'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f"Article id = {post_id}")


def addpage(request):
    return HttpResponse("Add article")


def contact(request):
    return HttpResponse("Feedback")


def login(request):
    return HttpResponse("Log in")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")