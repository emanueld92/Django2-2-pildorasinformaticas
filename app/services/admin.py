from django.contrib import admin
from .models import service
# Register your models here.
#class ServiceAdmin(admin.ModelAdmin):
 #   readonly_fields=('created')

admin.site.register(service)