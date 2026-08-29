from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    data = {
        'title': 'Home',
        'content': "Главная страница",
        'name': 'maks',
        'id': '12345',
        'list': [1,2,3],
        'dict': {'key': 50}
    }
    return render(request,'main/index.html',data)

def about(request):
    return HttpResponse('About page')