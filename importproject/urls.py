"""importproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path as url

from django.conf import settings

from django.views.static import serve


from django.contrib import admin
from django.urls import path
from exportapp import views





urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
    path('admin/', admin.site.urls, name="admin"),
    path('about_company/', views.about_index, name="about_company"),
    path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    path('certification/', views.certification, name="certification"),
    path('contact_us/', views.contact, name="contact_us"),
    path('gallery/', views.gallery, name="gallery"),
   
    path('sourcing_agent/', views.sourcing_agent, name="sourcing_agent"),
    path('key_person/', views.key_person, name="key_person"),
    path('incense/', views.incense, name="incense"),
    path('candles/', views.candles, name="candles"),
   
    path('wood/', views.wood, name="wood"),
    path('bamboo/', views.bamboo, name="bamboo"),
    path('clay/', views.clay, name="clay"),

]



