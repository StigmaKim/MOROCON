from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from Robocon.view import main, map, missionInfo, search, mapManage, mapAdd, mapAddPro, mapDelete, robot, robotAdd,\
    robotAddPro, robotSelectForm
from django.http.request import HttpRequest

urlpatterns = patterns('',
                       url(r'^$', main),
                       url(r'^main/', main),
                       url(r'^map/', map),
                       url(r'^mission_info/', missionInfo),
                       url(r'^search/', search),
                       url(r'^map_manage/', mapManage),
                       url(r'^map_add/', mapAdd),
                       url(r'^map_add_pro/', mapAddPro),
                       url(r'^map_delete/', mapDelete),
                       url(r'^robot/', robot),
                       url(r'^robot_add/', robotAdd),
                       url(r'^robot_add_pro/', robotAddPro),
                       url(r'^robot_select/', robotSelectForm)
    # Examples:
    # url(r'^$', 'SE2.views.home', name='home'),
    # url(r'^SE2/', include('SE2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
