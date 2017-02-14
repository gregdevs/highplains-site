from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from homeapp.models import MainNav


# Create your views here.

def contact(request):
	nav_items = MainNav.objects.all().order_by('nav_position')
	return render(request, 'homeapp/contact.html', {'nav_items': nav_items, 'template_name': 'contact'})	

