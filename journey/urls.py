from django.conf.urls.defaults import *
import os
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '', 
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.curdir + '/site_media'}),
    (r'^my_votes/$', 'journey.vote.views.get_my_votes'),
    (r'^login/$', 'journey.creds.views.user_login'),
    (r'^logout/$', 'journey.creds.views.logout'),
)
