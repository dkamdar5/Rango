from django.contrib import admin
from rango.models import Category, Page

#register application models with admin
admin.site.register(Category)
admin.site.register(Page)