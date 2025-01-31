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
    price = models.PositiveIntegerField()
    stocks = models.PositiveIntegerField()
    slug = AutoSlugField(populate_from='product_name', unique_with='seller')
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, default="No_Image_Available.jpg")
    seller = models.ForeignKey(
        MarketplaceUser,
        on_delete=models.CASCADE,
        related_name='products'
        )

    def __str__(self):
            return self.product_name
    
class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(MarketplaceUser, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    orderedAt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.orderID}-{self.product}-{self.user}"
    
    def calculate_total_price(self):
        self.total_price = (self.product.price) * (self.quantity)
        return self.total_price
    
class Cart(models.Model):
    cartID = models.AutoField(primary_key=True)
    user = models.ForeignKey(MarketplaceUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    
         

