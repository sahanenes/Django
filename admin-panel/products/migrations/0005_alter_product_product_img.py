# Generated by Django 4.1.5 on 2023-01-21 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(blank=True, default='defaults/520446-1181524783.jpg', null=True, upload_to='product/'),
        ),
    ]