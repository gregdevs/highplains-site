from __future__ import unicode_literals

from django.db import models
# Create your models here.



class OurProject(models.Model):
	project_title = models.CharField(max_length=140, null=True)
	text_area = models.TextField(default="project text")
	slug = models.SlugField(max_length=40)

	def __str__(self):
		return self.project_title

