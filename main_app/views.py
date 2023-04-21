from django.shortcuts import render

from .models import Coin

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def coins_index(request):
    coins = Coin.objects.all()
    return render(request, 'coins/index.html', {
        'coins': coins
    })