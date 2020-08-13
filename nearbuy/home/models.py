from django.db import models
from datetime import datetime

# Create your models here.
class Store(models.Model):     
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=25) 
    is_open = models.BooleanField(default=False)
    image = models.FileField(upload_to='home/storeimages', blank=True)
    is_delivering = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)    # date saved on db
    #location =  models.PointField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name =  models.CharField(max_length=100)
    category = models.CharField(max_length=25)
    price = models.DecimalField(decimal_places=2,max_digits=5)
    is_digital = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
