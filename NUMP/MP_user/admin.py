from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Product, MarketplaceUser

class MarketplaceUserInLine(admin.StackedInline):
    model = MarketplaceUser
    can_delete= False
    verbose_name_plural = 'Marketplace_user'

class UserAdmin(BaseUserAdmin):
    inlines = [MarketplaceUserInLine]

# Register your models here.
admin.site.register(MarketplaceUser)
admin.site.register(Product)