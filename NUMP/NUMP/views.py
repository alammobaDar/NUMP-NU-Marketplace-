from django.shortcuts import render, get_object_or_404
from MP_user.models import Product

def home(request):  
    product = Product.objects.all()
    return render(request, 'home.html', {'product': product})

def product_info(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_info_home.html', {'product': product})