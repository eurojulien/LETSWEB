from django.conf.urls import patterns, url

from LETSBOOK import views

urlpatterns = patterns('',

    url(r'find_book', views.findBook, name='findBook'),

)