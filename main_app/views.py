from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

def coins_detail(request, coin_id):
    coin = Coin.objects.get(id=coin_id)
    return render(request, 'coins/detail.html', {
        'coin': coin
    })

class CoinCreate(CreateView):
    model = Coin
    fields = '__all__'
    success_url = '/coins/{coin_id}'

class CoinUpdate(UpdateView):
    model = Coin
    fields = ['country', 'state', 'value', 'year', 'description']

class CoinDelete(DeleteView):
    model = Coin
    success_url = '/coins'