from django.db import models

# Create your models here.

class MarketplaceUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=75)
    contact = models.CharField(max_length=11)  
    createdAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    createdAt = models.DateField(auto_now_add=True)
    description = models.TextField()
    price = models.FloatField()
    stocks = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')
    seller = models.ForeignKey(
        MarketplaceUser,
        on_delete=models.CASCADE,
        related_name='products'
        )

    def __str__(self):
            return self.product_name