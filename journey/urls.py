from django.conf.urls.defaults import *
import os
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '', 
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.curdir + '/site_media'}),
    (r'^my_votes/$', 'journey.vote.views.get_my_votes'),
    (r'^vote/$', 'journey.vote.views.vote'),
    (r'^login/$', 'journey.creds.views.user_login'),
    (r'^logout/$', 'journey.creds.views.logout_user'),
    (r'^register/$', 'journey.creds.views.register'),
    (r'^project/$', 'journey.vote.views.project'),
    (r'^add_myself_to_team/$', 'journey.vote.views.add_myself_to_team'),
    (r'^m/$', 'journey.static_html.views.mobile'),
    (r'^ballot/$', 'journey.static_html.views.ballot'),
    (r'^$', 'journey.static_html.views.ballot'),
    (r'^admin/', include(admin.site.urls)),
        
)
