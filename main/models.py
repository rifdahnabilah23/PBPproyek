from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    gambar = models.URLField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)