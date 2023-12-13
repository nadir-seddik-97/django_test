from django.db import models
from .store import Store

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to ='products/',null=True)

    def __str__(self):
        return f"{self.name} {self.store.name}"  