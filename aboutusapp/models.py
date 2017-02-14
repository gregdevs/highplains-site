from __future__ import unicode_literals

from django.db import models

# Create your models here.


class AboutUs(models.Model):
	about_us_text = models.TextField()


	def __str__(self):
		return self.about_us_text