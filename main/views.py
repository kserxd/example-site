from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title': 'Главная',
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})

def contact(request):
    return render(request, 'main/contact.html', {'title': 'Контактная информация'})
