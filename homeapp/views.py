from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template

from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import HomeProject, HomeBucket, HomeAbout, MainNav
from django.conf import settings
import os,sys
# Create your views here.
import logging, logging.config

import json

def home(request):
  buckets = HomeBucket.objects.all().order_by('bucket_title')
  about_us = HomeAbout.objects.all()
  projects = HomeProject.objects.all().order_by('id')
  nav_items = MainNav.objects.all().order_by('nav_position')
  slideshow_list = os.listdir(os.path.join(settings.STATIC_ROOT, "img/slideshow/"));
  proj_list = [] 
  for project in projects:
    thisproj = str(project).lower().replace(" ", "").replace("'", "")
    thisprojid = project.project.id
    thisprojslug = project.project.slug
    thisprojtitle = project.project.project_title
    this_dict = { "projname":thisproj, "projid": thisprojid, "projslug": thisprojslug, "projtitle": thisprojtitle }
    proj_list.append(this_dict)

  hero_photos = []
  slideshow = []

  for img in slideshow_list:
    slideshow.append(img) 

  for p in proj_list:
    pthumbs = os.listdir(os.path.join(settings.STATIC_ROOT, "img/projects/" + p['projname'] + '/web/'))

    for t in pthumbs:
      if "main" in t:
        hero_dict = {"proj": p['projname'], "projid": p['projid'], "projtitle": p["projtitle"], "projslug": p["projslug"],"hero": t}
        hero_photos.append(hero_dict)  
  logging.info(slideshow)      
  return render(request, 'homeapp/home.html',  {'slideshow_images': slideshow, 'buckets': buckets, 'about_us': about_us, 'projects': hero_photos, 'nav_items': nav_items, 'template_name': 'home'})


def create_post(request):
  if request.method == 'POST':
    post_text = request.POST
    contact_name = post_text.__getitem__('dataMsg[name]')        
    contact_email = post_text.__getitem__('dataMsg[email]')
    form_content = post_text.__getitem__('dataMsg[message]')
    template = get_template('homeapp/contact_template.txt')
    context = Context({'contact_name': contact_name,'contact_email': contact_email, 'form_content':form_content,})
    content = template.render(context)
    email = EmailMessage("New Contact form submission", content, "Your website" + '', [''], headers = {'Reply-To': contact_email })
    email.send()
 

    return HttpResponse(
      json.dumps("Success, Email Sent"),
        content_type="application/json"
      )
  else:
    return HttpResponse(
      json.dumps({"nothing to see": "this isn't happening"}),
        content_type="application/json"
      )