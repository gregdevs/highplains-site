from django.shortcuts import render
from .models import OurProject
from homeapp.models import MainNav
from django.http import HttpResponse
import logging, logging.config
import os,sys
from django.conf import settings
from django.template.defaultfilters import slugify
# Create your views here.
def ourprojects(request):
  our_projects = OurProject.objects.all()
  nav_items = MainNav.objects.all().order_by('nav_position')
  template_name = "our projects"
  proj_list = []

  for project in our_projects:
  	thisproj = str(project).lower().replace(" ", "").replace("'", "")
  	proj_list.append(thisproj)

  hero_photos = []

  for p in proj_list:
  	pthumbs = os.listdir(os.path.join(settings.STATIC_ROOT, "img/projects/" + p + '/web/'))

  	for t in pthumbs:
  	  if "main" in t:
  		  hero_dict = {"proj": p, "hero": t}
  		  hero_photos.append(hero_dict)

  return render(request, "homeapp/ourprojects.html", {'our_projects': our_projects, 'hero_photos': hero_photos, 'nav_items': nav_items, 'template_name': template_name})



def thisproject(request, slug):
	nav_items = MainNav.objects.all().order_by('nav_position')
	#kwargs = {'project_title__replaceapos': projectname}
	#return HttpResponse("this id is" + projectid)
	project_obj = OurProject.objects.filter(slug = slugify(slug))
	pthumbs = os.listdir(os.path.join(settings.STATIC_ROOT, "img/projects/" + project_obj[0].project_title.lower().replace(" ", "").replace("'", "") + '/web/'))
	project_thumbs_list = []

	for t in pthumbs:

		if not t.startswith('.'):
			project_thumbs_list.append(t)


	project_title = project_obj[0].project_title
	return render(request, "homeapp/project.html", {'project_obj': project_obj,  'project_thumbs': project_thumbs_list, 'nav_items': nav_items, 'template_name': project_title})