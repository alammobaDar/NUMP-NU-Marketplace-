from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("user:products")
    else:
        form = UserCreationForm()
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