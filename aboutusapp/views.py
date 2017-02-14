from django.shortcuts import render
from .models import AboutUs
from homeapp.models import MainNav

# Create your views here.
def aboutus(request):
	aboutus = AboutUs.objects.all()
	nav_items = MainNav.objects.all().order_by('nav_position')
	return render(request, 'homeapp/aboutus.html', {'aboutus': aboutus, 'template_name': 'about us', 'nav_items': nav_items})