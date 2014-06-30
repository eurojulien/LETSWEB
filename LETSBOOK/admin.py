from django.contrib import admin

# Register your models here.
from django.contrib import admin
from LETSBOOK.models import *

admin.site.register(Establishment)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Book)
admin.site.register(Account)