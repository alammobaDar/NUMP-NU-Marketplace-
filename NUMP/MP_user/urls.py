from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('', views.products_page, name='products'),
    path('MyWallet/', views.my_wallet_page, name='mywallet'),
    path('Profile/', views.profile_page, name='profile'),
    path('NewProduct/', views.new_product, name="new_product"),
    path('<slug:slug>', views.product_info_page, name='product_info'),
    path('delete/<int:id>', views.delete, name="delete"),
    path('AddToCart/', views.cart_page, name='cart'),
    path('Order/', views.order_page, name="order"),
    path('BuyProduct/<int:id>', views.buy_product, name='buy_product')
]