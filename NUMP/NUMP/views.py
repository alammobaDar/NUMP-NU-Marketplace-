from django.shortcuts import render, get_object_or_404, redirect
from MP_user.models import Product, MarketplaceUser, Order, Cart
from MP_user.forms import BuyProduct, CartProduct
from django.contrib.auth.decorators import login_required


def home(request):  
    product = Product.objects.all()
    return render(request, 'home.html', {'product': product})


@login_required(login_url='userAuth/login/')
def product_info(request, slug):
    product = get_object_or_404(Product, slug=slug)
    mp_user = get_object_or_404(MarketplaceUser, user_name =request.user)

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "buy_now":
            buy_form = BuyProduct(request.POST)
            cart_form = CartProduct()
            
            if buy_form.is_valid():
                order = buy_form.save(commit=False)
                order.product = product
                order.user = mp_user
                order.total_price = order.calculate_total_price()
                order.save()
                seller = order.product.seller
                seller.revenue += order.total_price
                seller.save()
                # seller_wallet, created = Wallet.objects.get_or_create(user=order.product.seller, product=order.product)
                # seller_wallet.add_revenue(order.total_price)
                return redirect("user:order")
            
        if action == "add_to_cart":
            cart_form = CartProduct(request.POST)
            buy_form = BuyProduct()

            if cart_form.is_valid():
                cart_item, created = Cart.objects.get_or_create(
                    product=product,
                    user=mp_user,
                    defaults={"quantity": cart_form.cleaned_data["quantity"]}
                )
                if not created:
                    cart_item.quantity += cart_form.cleaned_data["quantity"]
                    cart_item.save()
                return redirect("user:cart")

    else:
        buy_form = BuyProduct()  
        cart_form = CartProduct()
    return render(request, 'product_info_home.html', {'product': product,
                                                      'buy_form':buy_form,
                                                      'cart_form':cart_form})


    