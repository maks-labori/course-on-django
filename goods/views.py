from django.shortcuts import render
from django.http import HttpResponse

import goods
from goods.models import Categories, Products
# Create your views here.

def catalog(request):
    goods = Products.objects.all()
    categories = Categories.objects.all()
    data ={
        'title':'Home - Каталог',
        'goods': goods,
        'categories':categories,
    }
    return render(request,'goods/catalog.html',data)

def product(request):
    return render(request,'goods/product.html') 