from django.conf.urls import patterns, include, url
#from login.views import login
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from userpanel.views import UserView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rrs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
    #url(r'^login/', include('login.urls', namespace="login")),
    url(r'^login/$', 'login.views.user_login'),
    url(r'^userpanel/$', login_required(UserView.as_view()), name='users'),
    url(r'^admin/', include(admin.site.urls)),
)
