from django.conf.urls import patterns, url

from LETSBOOK import views

urlpatterns = patterns('',

    url(r'school',       views.school,      name='school'),
    url(r'course',       views.course,      name='course'),
    url(r'book',         views.book,        name='book'),
    url(r'user',         views.user,        name='user'),

)