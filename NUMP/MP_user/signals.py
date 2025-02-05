from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import MarketplaceUser, Wallet

def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        MarketplaceUser.objects.create(user=instance)
    else:
        instance.mpuser.save()

    
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)