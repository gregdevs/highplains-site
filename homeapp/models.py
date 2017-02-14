from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from ourprojectsapp.models import OurProject

# Create your models here.
class MainNav(models.Model):
	nav_item = models.CharField(max_length=50)
	nav_position = models.IntegerField(default=1)

	class Meta:
		ordering = ["nav_position"]
	
	def __str__(self):
		return self.nav_item


class HomeBucket(models.Model):
	bucket_title = models.CharField(max_length=140)
	bucket_image = models.CharField(max_length=300, default="bucket_image")
	bucket_desc = models.TextField(default="bucket_desc")

	def __str__(self):
	  return self.bucket_title


class HomeAbout(models.Model):
	aboutus_headline = models.CharField(max_length=140)
	aboutus_desc = models.TextField(default="About US Description")

	def __str__(self):
	  return self.aboutus_headline	


class HomeProject(models.Model):
	project = models.ForeignKey(OurProject)

	def __unicode__(self):
	  return self.project.project_title