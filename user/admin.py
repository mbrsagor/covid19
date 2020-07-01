from django.contrib import admin
from .models import *


class RoleAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'role',
        'created_date'
    )

    search_fields = ['user', 'role']
    list_display_links = ['user']
    list_filter = ['user', 'role']
    list_per_page = 6


admin.site.register(Role, RoleAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'email', 'date_of_birth', 'gender',
        'mobile', 'address', 'bio', 'created_at', 'updated_at'
    )


admin.site.register(Profile, ProfileAdmin)
