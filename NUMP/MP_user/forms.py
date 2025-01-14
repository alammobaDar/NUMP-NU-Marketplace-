from django import forms
from . import models

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