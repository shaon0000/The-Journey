from django.conf.urls.defaults import *
import os
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('', 
	('r^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.getcwd() + '/site_media'}),
)
