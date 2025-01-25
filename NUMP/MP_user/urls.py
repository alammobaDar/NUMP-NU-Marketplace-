from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('', views.products_page, name='products'),
    path('MyWallet/', views.my_wallet_page, name='mywallet'),
    path('Profile/', views.profile_page, name='profile'),
    path("NewProduct/", views.new_product, name="new_product"),
    path('<slug:slug>', views.product_info_page, name='product_info'),
    path("delete/<int:id>", views.delete, name="delete"),
]    # path("update/<int:id>", views.update, name='update')
