from django.db import models
from datetime import datetime

# Create your models here.
class Store(models.Model):     
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=25) 
    is_open = models.BooleanField(default=False)
    image = models.FileField(upload_to='home/storeimages', blank=True)
    is_delivering = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name