# Generated by Django 4.2.6 on 2023-12-11 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt_main', '0004_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(null=True, upload_to='products/'),
        ),
    ]
