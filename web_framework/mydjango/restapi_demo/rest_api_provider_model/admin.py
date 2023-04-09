# Register your models here.
from django.contrib import admin

from .models import Subject, Teacher

admin.site.register(Subject)
admin.site.register(Teacher)

admin.site.site_header = 'rest-api-demo'
admin.site.site_title = 'rest-api-demo-admin'
admin.site.index_title = 'welcome'
