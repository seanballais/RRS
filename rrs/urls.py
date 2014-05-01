from django.conf.urls import patterns, include, url
from login.views import UserPanel, hello

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rrs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', UserPanel),
    url(r'^login/1', UserPanel),
    url(r'^admin/', include(admin.site.urls)),
)
