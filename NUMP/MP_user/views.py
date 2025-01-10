from django.shortcuts import render
from .models import Product


# Create your views here.
def products_page(request):
    product = Product.objects.all()
    return render(request, 'mp_user/CreateProductDisplay.html', {'product': product})

def my_wallet_page(request):
    return render(request, 'mp_user/MyWallet.html')

def profile_page(request):
    return render(request, 'mp_user/Profile.html')