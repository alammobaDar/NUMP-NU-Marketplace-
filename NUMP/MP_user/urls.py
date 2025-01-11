from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('Products/', views.products_page, name='products'),
    path('MyWallet/', views.my_wallet_page, name='mywallet'),
    path('Profile/', views.profile_page, name='profile'),
    path('ProductInformation/', views.product_info_page, name='product_info')
]