from django.shortcuts import render, get_object_or_404, redirect
from MP_user.models import Product, MarketplaceUser, Order
from MP_user.forms import BuyProduct


def home(request):  
    product = Product.objects.all()
    return render(request, 'home.html', {'product': product})

def product_info(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == "POST":
        form = BuyProduct(request.POST)
        if form.is_valid():
            mp_user = get_object_or_404(MarketplaceUser, user_name =request.user)
            order = form.save(commit=False)
            order.product = product
            order.user = mp_user
            order.total_price = order.calculate_total_price()
            order.save()
            return redirect("user:order")
    else:
        form = BuyProduct()  
    return render(request, 'product_info_home.html', {'form':form, 'product': product})




    