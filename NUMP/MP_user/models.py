from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.

class MarketplaceUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mpuser')
    contact = models.CharField(max_length=11)  
    createdAt = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.user_name.username

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    createdAt = models.DateField(auto_now_add=True)
    description = models.TextField()
    price = models.FloatField()
    stocks = models.IntegerField()
    slug = AutoSlugField(populate_from='product_name', unique_with='seller')
    image = models.ImageField(upload_to='product_images/')
    seller = models.ForeignKey(
        MarketplaceUser,
        on_delete=models.CASCADE,
        related_name='products'
        )

    def __str__(self):
            return self.product_name