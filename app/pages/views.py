from django.shortcuts import render, get_object_or_404
from .models import Food


def index(request):
    context = {
        "pizza": Food.objects.filter(food_type="Pizza"),
        "sushi": Food.objects.filter(food_type='Sushi'),
        "dessert": Food.objects.filter(food_type='Dessert'),
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')


def menu(request):
    return render(request, 'pages/menu.html')


def blog(request):
    return render(request, 'pages/blog.html')


def contact(request):
    return render(request, 'pages/contact.html')


def elements(request):
    return render(request, 'pages/elements.html')
