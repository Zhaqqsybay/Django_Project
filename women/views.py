from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "Car Dealer App", 'url_name': 'about'},
        {'title': "All Brands", 'url_name': 'add_page'},
        {'title': "All Dealers", 'url_name': 'contact'},
        {'title': "Login", 'url_name': 'login'}
]


def index(request):
    posts = Car.objects.all()
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Car Dear',
        'cat_selected': 0,
    }

    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Car Dealer App'})


def addpage(request):
    return HttpResponse("All Brands")

def contact(request):
    return HttpResponse("All Dealers")

def login(request):
    return HttpResponse("Login")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def show_category(request, cat_id):
    posts = Car.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context)

