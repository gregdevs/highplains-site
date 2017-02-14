from django.shortcuts import render
from django.http import HttpResponse
import logging, logging.config
from django.conf import settings
from .models import Product
from homeapp.models import MainNav
import os,sys
# Create your views here.

def prodview(request, productname=None):
	nav_items = MainNav.objects.all().order_by('nav_position')
	if productname is not None:
		pname = productname
		product = Product.objects.filter(product_name = pname)
	else:
		pname = request.get_full_path().replace('/', '').lower()
		product = Product.objects.filter(product_name = pname)
	#thumb_list = []
	
	#for t in  pthumbs:
		#if not t.startswith('.'):
			#thumb_list.append(t)
	
	pthumbs = os.listdir(os.path.join(settings.STATIC_ROOT, "img/products/" + pname + '/web/'))
	
	return render(request, 'homeapp/products.html', {'product': product, 'product_thumbs': pthumbs, 'nav_items': nav_items, 'template_name': pname})
