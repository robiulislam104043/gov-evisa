from django.contrib import admin

from .models import VisaRecord

admin.site.site_header = 'Govt-eVisa Administration'
admin.site.site_title = 'Govt-eVisa Portal'
admin.site.index_title = 'Welcome to Govt-eVisa Dashboard'


@admin.register(VisaRecord)
class VisaRecordAdmin(admin.ModelAdmin):
    list_display = (
        'visa_number',
        'passport_number',
        'visa_status',
        'citizenship',
    )
    list_filter = ('visa_status', 'visa_type')
    search_fields = (
        'visa_number',
        'passport_number',
    )
