from django.contrib import admin
from .models import DataProfile
# Register your models here.

class dataManager(admin.ModelAdmin):
    list_display = ['id','TDS','PH','TU','TEM','created_time']
    search_fields = ['created_time']

admin.site.register(DataProfile, dataManager)