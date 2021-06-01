from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime


class Category(models.Model):
	name = models.CharField(max_length=20, unique=True)\

	def __str__(self):
		return self.name

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

class Highlight(models.Model):
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    image = models.ImageField(null=True, blank=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT,editable=False , null=True)
    total = models.IntegerField(null=True)
    content = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    numberphone = models.CharField(max_length=100, null=True)

class HighlightBig(models.Model):
	description = models.CharField(max_length=50)
	category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
	image = models.ImageField(null=True, blank=True)
