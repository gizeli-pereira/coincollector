from django.shortcuts import render

coins = [
  {'value': 'Quarter', 'state': 'Maryland'},
  {'value': 'Quarter', 'state': 'Texas'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def coins_index(request):
    return render(request, 'coins/index.html', {
        'coins': coins
    })