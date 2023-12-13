from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class Users(AbstractUser):


    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=100, null=True)
    photo = models.ImageField(upload_to ='images/', default='images/user.jpeg')

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 
