from django.contrib import admin
from .models import *


class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'organization_name', 'designation', 'job_year',
        'created_at', 'updated_at'
    )

    search_fields = ['organization_name', 'designation', 'job_year']
    list_display_links = ['organization_name', 'designation']
    list_filter = ['organization_name', 'designation']

    list_per_page = 6


admin.site.register(Experience, ExperienceAdmin)


class AvailabilityAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'day', 'time', 'date',
        'created_at', 'updated_at'
    )

    search_fields = ['day', 'time', 'day']
    list_display_links = ['day']
    list_filter = ['day', 'time', 'date']
    list_editable = ['date', 'time']

    list_per_page = 6


admin.site.register(Availability, AvailabilityAdmin)


class LaboratoriesAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'lab_name', 'machinery_name', 'total_machinery',
        'created_at', 'updated_at'
    )

    search_fields = ['lab_name', 'machinery_name']
    list_display_links = ['lab_name']
    list_filter = ['lab_name', 'machinery_name', 'total_machinery']
    list_editable = ['total_machinery']

    list_per_page = 6


admin.site.register(Laboratories, LaboratoriesAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'department_name', 'employee_type',
        'created_at', 'updated_at'
    )

    search_fields = ['department_name', 'employee_type']
    list_display_links = ['department_name']
    list_filter = ['department_name', 'employee_type']

    list_per_page = 6


admin.site.register(Department, DepartmentAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'service_name', 'price', 'discount_price',
        'laboratories', 'created_at', 'updated_at'
    )
    search_fields = ['service_name', 'price']
    list_display_links = ['service_name', 'laboratories']
    list_filter = ['service_name', 'price', 'laboratories']
    list_editable = ['price', 'discount_price']
    list_per_page = 6


admin.site.register(Service, ServiceAdmin)
