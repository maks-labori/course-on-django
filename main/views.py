from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    data = {
        'title': 'Home - Главная',
        'content': "Магазин мебели HOME"
    }
    return render(request,'main/index.html',data)

def about(request):
    data = {
            'title': 'Home - О нас',
            'content': "About our",
            'text_on_page': "text for our market"
        }
    return render(request,'main/about.html',data)