from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Section administrative
    url(r'^admin/', include(admin.site.urls)),

    # LETSBOOK
    url(r'^$', include('LETSBOOK.urls')),
)
