from django.conf.urls import patterns, include, url
from django.views import generic

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'hack.views.home', name='home'),
    url(r'^new_event', 'hack.views.new_event', name='new_event'),
    url(r'^(?P<event_id>[0-9]+)/update/$', 'hack.views.update', name='update'),
 	url(r'^(?P<event_id>[0-9]+)/$', 'hack.views.event_page', name='event_page'),
 	url(r'^(?P<event_id>[0-9]+)/save_update$', 'hack.views.save_update', name='save_update'),
    # url(r'^hack/', include('hack.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
