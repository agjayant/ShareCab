"""sharecab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   url(r'^$', 'sharecabapp.views.home', name='home'),
   url(r'^home', 'sharecabapp.views.home', name='home'),
   url(r'^insert', 'sharecabapp.views.insert', name='insert'),
   url(r'^entry', 'sharecabapp.views.entry', name='entry'),
   url(r'^thankyou', 'sharecabapp.views.thankyou', name='thankyou'),
   url(r'^query', 'sharecabapp.views.query', name='query'),
   url(r'^result', 'sharecabapp.views.result', name='result'),
   url(r'^profile', 'sharecabapp.views.profile', name='profile'),
   url(r'^ridepage/?P<id>([0-9]+)/$', 'sharecabapp.views.ridepage', name='ridepage'),
   url(r'^addComment', 'sharecabapp.views.addComment', name='addComment'),
   url(r'^admin/', include(admin.site.urls)),
   url('', include('social.apps.django_app.urls', namespace='social')),
   url('', include('django.contrib.auth.urls', namespace='auth')),
)

