# Generated by Django 5.1.4 on 2025-01-10 05:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketplaceUser',
            fields=[
                ('seller_id', models.AutoField(primary_key=True, serialize=False)),
                ('seller_name', models.CharField(max_length=75)),
                ('contact', models.CharField(max_length=11)),
                ('createdAt', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('stocks', models.IntegerField()),
                ('image', models.ImageField(upload_to='product_images/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='MP_user.marketplaceuser')),
            ],
        ),
    ]