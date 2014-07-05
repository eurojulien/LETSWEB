from django.conf.urls import patterns, url

from LETSBOOK import views

urlpatterns = patterns('',

    url(r'school',       views.school,      name='school'),
    url(r'department',   views.addModifyDepartment,  name='addModifyDepartment'),
    url(r'course',       views.addModifyCourse,      name='addModifyCourse'),
    url(r'book',         views.book,        name='book'),

)