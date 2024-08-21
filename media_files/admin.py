from django.contrib import admin
from .models import UploadLogs

# Register your models here.
@admin.register(UploadLogs)
class UploadLogsAdmin(admin.ModelAdmin):
    list_display = ('form_id', 'form_name', 'file_name', 'created_at', 'status', 'created_by')
    list_filter = ('form_name', 'status')
    search_fields = ('form_name', 'file_name', 'created_by__username')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)