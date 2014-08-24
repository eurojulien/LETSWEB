from django.conf.urls import patterns, url
from LETSBOOK import views

urlpatterns = patterns('',

    # Index du site
    url(r'^$',          views.index),
    )