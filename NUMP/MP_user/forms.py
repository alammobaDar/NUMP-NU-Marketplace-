from pyexpat import model
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateProduct(forms.ModelForm):
    class Meta:
        model = models.Product
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
            'username', 'contact', 'password1', 'password2'
        ]