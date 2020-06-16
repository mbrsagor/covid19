from django.contrib import admin
from .models import *


# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'parent', 'is_active',
        'created_at', 'updated_at'
    )

    list_display_links = ['name']

    list_filter = [
        'name', 'parent'
    ]

    list_per_page = 6


admin.site.register(Location, LocationAdmin)


class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'disease_name', 'created_at', 'updated_at')


admin.site.register(Disease, DiseaseAdmin)


class ContagionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'disease', 'country', 'reporter',
        'daily_test', 'daily_effected', 'daily_dies',
        'daily_recovery', 'created_at', 'updated_at'
    )

    list_display_links = (
        'disease', 'country', 'daily_effected'
    )

    search_fields = ['daily_test', 'daily_effected', 'daily_dies']
    list_editable = ['daily_test', 'daily_dies', 'daily_recovery']
    list_per_page = 6
    list_filter = ['daily_test', 'daily_effected', 'daily_dies']


admin.site.register(Contagion, ContagionAdmin)
