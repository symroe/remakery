from django.conf.urls import patterns, include, url
from filebrowser.sites import site as fb_site

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # Examples:
    # url(r'^$', 'remakery.views.home', name='home'),
    # url(r'^remakery/', include('remakery.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/filebrowser/', include(fb_site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^mce_filebrowser/', include('mce_filebrowser.urls')),
)

urlpatterns += patterns('',
    url(r'', include('feincms.urls')),
)
