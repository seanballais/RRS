from django.conf.urls import patterns, include, url
#from login.views import login
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rrs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
    #url(r'^login/', include('login.urls', namespace="login")),
    url(r'^login/$', 'login.views.user_login'),
    url(r'^userpanel/$', 'userpanel.views.userpanel'),
    url(r'^userpanel/room/(?P<room_id>\d+)/$', 'userpanel.views.room', name='room'),
    url(r'^userpanel/equipment/(?P<equipment_id>\d+)/$', 'userpanel.views.equipment', name='equipment'),
    url(r'^userpanel/event/(?P<reserveinfo_id>\d+)/$', 'userpanel.views.event', name='event'),
    url(r'^userpanel/use/(?P<useinfo_id>\d+)/$', 'userpanel.views.use', name='use'),
    url(r'^userpanel/(?P<room_id>\d+)/reserve/$', 'userpanel.views.reserve', name='reserve'),
    url(r'^admin/', include(admin.site.urls)),
)
