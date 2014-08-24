from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',

    # Section administrative
    url(r'^admin/', include(admin.site.urls)),

    # LETSBOOK
    url(r'^$', include('LETSBOOK.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
