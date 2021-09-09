from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class resourceGarment (resources.ModelResource):
    class Meta:
        model = garment

class adminGarment(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['mark']
    list_display = ['client','price','discount']
    resource_class = resourceGarment

admin.site.register(garment, adminGarment)

class resourceMark(resources.ModelResource):
    class Meta:
        model = mark

class adminMark(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    resource_class = resourceMark

admin.site.register(mark, adminMark)




