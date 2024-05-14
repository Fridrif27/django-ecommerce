from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    context = {
        'title': '',
        'content': "",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': '',
        'content': "",
        'text_on_page': "Welcome to Games Core – your ultimate destination for all things gaming!"
    }

    return render(request, 'main/about.html', context)
