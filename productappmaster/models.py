from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class Product(models.Model):
	intro_text = models.TextField(default="Some Text")
	product_name = models.CharField(max_length=140)
	
	def __str__(self):
	  return self.product_name