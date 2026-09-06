from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from goods.models import Categories

def index(request):
    categories = Categories.objects.all()
    data = {
        'title': 'Home - Главная',
        'content': "Магазин мебели HOME",
        'categories': categories,
    }
    return render(request,'main/index.html',data)

def about(request):
    categories = Categories.objects.all()

    data = {
            'title': 'Home - О нас',
            'content': "About our",
            'text_on_page': "text for our market",
            'categories': categories,
        }
    return render(request,'main/about.html',data)