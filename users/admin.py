from django.contrib import admin
from .models import UserProfile

# Register your models here.


class UserManager(admin.ModelAdmin):
    list_display = ['username','password','phone','created_time','updated_time']
    list_display_links = ['username']
    list_filter = ['username']
    search_fields = ['username']

admin.site.register(UserProfile,UserManager)