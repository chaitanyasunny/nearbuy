from django.db import models

# Create your models here.
class store(models.Model):     
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=25) 
    is_open = models.BooleanField(default=False)
    image = models.FileField()
    is_delivering = models.BooleanField(default=False)

    def __str__(self):
        return self.name