from django.conf.urls import patterns, url

from LETSBOOK import views

urlpatterns = patterns('',

    url('school',       views.addModifySchool,      name='addModifySchool'),
    url('department',   views.addModifyDepartment,  name='addModifyDepartment'),
    url('course',       views.addModifyCourse,      name='addModifyCourse'),
    url(r'book',        views.addModififyBook,      name='addModifyBook'),
    url(r'findBook',    views.findBook,             name='findBook'),

)