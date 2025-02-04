from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from MP_user.forms import SignupForms
from MP_user.models import MarketplaceUser

# Create your views here.

def register(request):
    if request.method == "POST":
        form = SignupForms(request.POST)
        if form.is_valid():
            login(request, form.save())
            username = form.cleaned_data.get('username')
            contact = form.cleaned_data.get('contact')
            email = form.cleaned_data.get('email')
            user = User.objects.get(username=username)
            user_data = MarketplaceUser.objects.create(user_name=user, contact=contact, email=email)
            user_data.save()
            return redirect("user:products")
    else:
        form = SignupForms()
    return render(request, 'userAuth/register.html', { 'form':form })


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("user:products")
    else:
        form = AuthenticationForm()
    return render(request, 'userAuth/login.html', { 'form':form })

def sign_out(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")