from django.contrib import admin
from .models import MainNav, HomeAbout, HomeBucket, HomeProject
# Register your models here.
admin.site.register([MainNav, HomeProject, HomeBucket, HomeAbout])