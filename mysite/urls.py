"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from aboutusapp import views as aboutusviews
from homeapp import views as homeviews
from ourprojectsapp import views as ourprojectsviews
from contactapp import views as contactviews
from productappmaster import views as productviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homeviews.home, name="home"),
    url(r'^create_post/', homeviews.create_post, name="create_post"),    
    #url(r'^decor/', furnitureviews.furniture, name="decor"),
    url(r'^aboutus/', aboutusviews.aboutus, name="aboutus"),
    url(r'^ourprojects/(?P<slug>.+)', ourprojectsviews.thisproject),    
    url(r'^ourprojects/', ourprojectsviews.ourprojects, name="ourprojects"),
    url(r'^contact/', contactviews.contact, name="contact"),
    url(r'^product/(?P<productname>.+)', productviews.prodview),
    url(r'^decor/', productviews.prodview, name="decor"),    
    #url(r'^metal/', include('metal.urls')),
    #url(r'^admin/', admin.site.urls),
]
