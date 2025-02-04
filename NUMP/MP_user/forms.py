from pyexpat import model
from django import forms
from . import models
from .models import MarketplaceUser, Order, Cart, Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'description', 
            'price', 
            'stocks', 
            'image'
            ]
        
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image and not self.instance.pk:
            raise forms.ValidationError("An image is required when creating a product.")
        return image
    

class SignupForms(UserCreationForm):
    contact = forms.CharField()

    class Meta:
        model = User
        fields = [
            'username', 'contact', 'email', 'password1', 'password2'
        ]


class BuyProduct(forms.ModelForm):
    class Meta:
        model = Order

        fields = [
            'quantity'
        ]

class CartProduct(forms.ModelForm):
    class Meta:
        model = Cart
        fields = [
            'quantity'
        ]

class EditProfile(forms.ModelForm):
    contact = forms.CharField()
    class Meta:
        model = MarketplaceUser()
        fields = [
            'user_name', 'contact', 'email', 'picture'
        ]
