# Generated by Django 4.2.6 on 2023-12-11 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt_main', '0002_users_address_alter_users_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='photo',
            field=models.ImageField(default='images/user.jpeg', upload_to='images/'),
        ),
    ]
