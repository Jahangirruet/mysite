from django.db import models

# Create your models here.
class ProductDetails(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField()
    size =  models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    discount = models.IntegerField()
    discription = models.CharField(max_length=100)
    spefication = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)


