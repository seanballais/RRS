from django.conf.urls import patterns, include, url
from login.views import login
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rrs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', 'login.views.login'),
    url(r'^admin/', include(admin.site.urls)),
)
