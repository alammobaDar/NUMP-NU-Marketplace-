from django.shortcuts import render
from MP_user.models import Product

def home(request):
    product = Product.objects.all()
    return render(request, 'home.html', {'product': product})