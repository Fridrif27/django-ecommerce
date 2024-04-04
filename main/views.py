from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context = {
        'title': '',
        'content': "",
        'categories': categories
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': '',
        'content': "",
        'text_on_page': "Welcome to Games Hub – your ultimate destination for all things gaming!"
    }

    return render(request, 'main/about.html', context)