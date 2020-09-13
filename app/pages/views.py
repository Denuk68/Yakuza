from django.shortcuts import render, get_object_or_404
from .models import Pizza, Sushi, Dessert, New


def index(request):

    context = {
        "pizza": Pizza.objects.all(),
        "sushi": Sushi.objects.all(),
        "dessert": Dessert.objects.all(),
        "new": New.objects.all(),
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')


def menu(request):

    context = {
        "pizza": Pizza.objects.all(),
        "sushi": Sushi.objects.all(),
        "dessert": Dessert.objects.all(),   
    }
    return render(request, 'pages/menu.html', context)


def blog(request):
    return render(request, 'pages/blog.html')


def contact(request):
    return render(request, 'pages/contact.html')


def elements(request):
    return render(request, 'pages/elements.html')
