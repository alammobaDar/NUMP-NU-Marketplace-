from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('', views.products_page, name='products'),
    path('MyWallet/', views.my_wallet_page, name='mywallet'),
    path('Profile/', views.profile_page, name='profile'),
    path('<slug:slug>', views.product_info_page, name='product_info')
]