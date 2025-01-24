
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from .models import MarketplaceUser, Product
from .forms import CreateProduct


# Create your views here.
def products_page(request):
    mp_user = get_object_or_404(MarketplaceUser, user_name=request.user)
    product = Product.objects.filter(seller=mp_user)
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

def delete(request, id):
    product = Product.objects.get(product_id=id)
    product.delete()
    
    return redirect('user:products')

def update(request, id):
    product = Product.objects.get(product_id=id)
    if request.method == 'POST':
        form = CreateProduct(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('user:products')
    else:
        form = CreateProduct(instance=product)
    return render(request, 'mp_user/ProductInformation.html', {'form':form, 'product':product})
