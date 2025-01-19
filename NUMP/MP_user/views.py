
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from .models import MarketplaceUser, Product
from .forms import CreateProduct


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
    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save(commit=False)
            mp_user = get_object_or_404(MarketplaceUser, user_name=request.user)
            new_product.seller = mp_user
            new_product.save()
            return redirect('user:products')
    else:
        form = CreateProduct()
    return render(request, 'mp_user/CreateProduct.html', {'form':form})