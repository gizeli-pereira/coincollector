from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.views.generic import ListView, DetailView
from .models import Coin, Imperfection
from .forms import FormatMaterialForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def coins_index(request):
    coins = Coin.objects.order_by('country')
    return render(request, 'coins/index.html', {
        'coins': coins
    })

def coins_detail(request, coin_id):
    coin = Coin.objects.get(id=coin_id)
    formatmaterial_form = FormatMaterialForm()
    return render(request, 'coins/detail.html', {
        'coin': coin, 'formatmaterial_form': formatmaterial_form
    })

def add_formatmaterial(request, coin_id):
    form = FormatMaterialForm(request.POST)
    if form.is_valid():
        new_formatmaterial = form.save(commit=False)
        new_formatmaterial.coin_id = coin_id
        new_formatmaterial.save()
    return redirect('detail', coin_id=coin_id)

class CoinCreate(CreateView):
    model = Coin
    fields = '__all__'

class CoinUpdate(UpdateView):
    model = Coin
    fields = ['country', 'state', 'value', 'year', 'description']

class CoinDelete(DeleteView):
    model = Coin
    success_url = '/coins'

class ImperfectionList(ListView):
  model = Imperfection

class ImperfectionDetail(DetailView):
  model = Imperfection

class ImperfectionCreate(CreateView):
  model = Imperfection
  fields = '__all__'

class ImperfectionUpdate(UpdateView):
  model = Imperfection
  fields = ['name']

class ImperfectionDelete(DeleteView):
  model = Imperfection
  success_url = '/imperfections'