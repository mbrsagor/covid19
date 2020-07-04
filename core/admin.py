from django.contrib import admin
from core.models.contagion import *


# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'is_active',
        'created_at', 'updated_at'
    )

    list_display_links = ['name']

    list_filter = ['name']

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


class HelpAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'help_text'
    )
    list_filter = (
        'id', 'title', 'help_text'
    )
    list_editable = ['title', 'help_text']
    list_per_page = 6


admin.site.register(Help, HelpAdmin)


class HospitalAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'hospital_name', 'location', 'hospital_type'
    )

    list_filter = (
        'hospital_name', 'location', 'hospital_type'
    )

    list_editable = ['location', 'hospital_type']
    list_per_page = 6


admin.site.register(Hospital, HospitalAdmin)
