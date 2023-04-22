from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('coins/', views.coins_index, name='index'),
    path('coins/<int:coin_id>', views.coins_detail, name='detail'),
    path('coins/create/', views.CoinCreate.as_view(), name='coins_create'),
]