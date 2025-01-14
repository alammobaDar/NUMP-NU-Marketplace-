from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.
def products_page(request):
    product = Product.objects.all()
    return render(request, 'mp_user/MyProduct.html', {'product': product})

def product_info_page(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'mp_user/ProductInformation.html', {'product': product})

def my_wallet_page(request):
    return render(request, 'mp_user/MyWallet.html')

def profile_page(request):
    return render(request, 'mp_user/Profile.html')

def new_product(request):
    return render(request, 'mp_user/CreateProduct.html')