from django.db import models
# Create your models here.
import datetime


class Category(models.Model):
	name = models.CharField(max_length=20, unique=True)

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

class Highlight(models.Model):
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

class Order(models.Model):
    pass
