from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from Robocon.view import main, map, mission_info

urlpatterns = patterns('',
                       url(r'^main/', main),
                       url(r'^map/', map),
                       url(r'^mission_info/', mission_info)
    # Examples:
    # url(r'^$', 'SE2.views.home', name='home'),
    # url(r'^SE2/', include('SE2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
