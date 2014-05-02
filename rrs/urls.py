from django.conf.urls import patterns, include, url
<<<<<<< HEAD
from login.views import user_login
=======
from login.views import UserPanel, hello

>>>>>>> 1a00bc241e1087cf3a15266eb5765240f10e1d0b
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rrs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

<<<<<<< HEAD
    url(r'^login/$', 'login.views.user_login'),
=======
    url(r'^login/', UserPanel),
    url(r'^login/1', UserPanel),
>>>>>>> 1a00bc241e1087cf3a15266eb5765240f10e1d0b
    url(r'^admin/', include(admin.site.urls)),
)
