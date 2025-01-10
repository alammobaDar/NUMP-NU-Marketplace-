from django.contrib import admin
from .models import Product, MarketplaceUser

# Register your models here.
admin.site.register(MarketplaceUser)
admin.site.register(Product)