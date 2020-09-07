from django.shortcuts import render



def index(request):
    return render(request, 'pages/index.html')

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