# Generated by Django 5.1.4 on 2025-01-11 14:50

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MP_user', '0002_rename_seller_id_marketplaceuser_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='product_name', unique_with=('seller', 'id')),
            preserve_default=False,
        ),
    ]
