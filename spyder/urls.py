from django.conf.urls import patterns, include, url
import webwiki.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spyder.views.home', name='home'),
    # url(r'^spyder/', include('spyder.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', webwiki.views.buildweb, name='home'),
    url(r'^refresh$', webwiki.views.refresh_page, name='refresh'),
    url(r'^spinweb/(.+)$', webwiki.views.spin_new_web, name='spin'),
)
