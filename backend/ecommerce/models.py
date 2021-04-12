from django.db import models
from django.contrib.auth.models import User
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
    user = models.ForeignKey(User, on_delete=models.PROTECT,editable=False , null=True)
    total = models.IntegerField(null=True)
    content = models.CharField(max_length=100, null=True)
