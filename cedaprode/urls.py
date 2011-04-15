from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import settings
from os import path as os_path

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cedaprode.views.home', name='home'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='user-login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='user-logout'),
    url(r'^', include('cedaprode.encuesta.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^files/(.*)$', 'django.views.static.serve',
                             {'document_root': os_path.join(settings.MEDIA_ROOT)}),
                           )
