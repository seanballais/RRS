from django.conf.urls import patterns, include, url
from django.contrib import admin
from login.views import index

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rrs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', index),
    url(r'^admin/', include(admin.site.urls)),
)
