# Generated by Django 5.1.4 on 2025-02-04 07:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MP_user', '0008_alter_product_price_alter_product_stocks_cart_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketplaceuser',
            name='picture',
            field=models.ImageField(blank=True, default='/No_profile.png', null=True, upload_to='UserProfile/'),
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=20)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MP_user.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MP_user.marketplaceuser')),
            ],
        ),
    ]
