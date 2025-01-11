from django.shortcuts import render
from .models import Product


# Create your views here.
def products_page(request):
    product = Product.objects.all()
    return render(request, 'mp_user/MyProduct.html', {'product': product})

def product_info_page(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'mp_user/ProductInformation.html', {'product': product})

def my_wallet_page(request):
    return render(request, 'mp_user/MyWallet.html')

def profile_page(request):
    return render(request, 'mp_user/Profile.html')