from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('coins/', views.coins_index, name='index'),
    path('coins/<int:coin_id>', views.coins_detail, name='detail'),
    path('coins/create/', views.CoinCreate.as_view(), name='coins_create'),
    path('coins/<int:pk>/update/', views.CoinUpdate.as_view(), name='coins_update'),
    path('coins/<int:pk>/delete/', views.CoinDelete.as_view(), name='coins_delete'),
    path('coins/<int:coin_id>/add_formatmaterial/', views.add_formatmaterial, name='add_formatmaterial'),
    path('coins/<int:coin_id>/assoc_imperfection/<int:imperfection_id>/', views.assoc_imperfection, name='assoc_imperfection'),
    path('coins/<int:coin_id>/unassoc_imperfection/<int:imperfection_id>/', views.unassoc_imperfection, name='unassoc_imperfection'),
    path('imperfections/', views.ImperfectionList.as_view(), name='imperfections_index'),
    path('imperfections/<int:pk>/', views.ImperfectionDetail.as_view(), name='imperfections_detail'),
    path('imperfections/create/', views.ImperfectionCreate.as_view(), name='imperfections_create'),
    path('imperfections/<int:pk>/update/', views.ImperfectionUpdate.as_view(), name='imperfections_update'),
    path('imperfections/<int:pk>/delete/', views.ImperfectionDelete.as_view(), name='imperfections_delete'),
    
]