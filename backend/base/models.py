from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    #image = 
    price = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    countInStock = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.name