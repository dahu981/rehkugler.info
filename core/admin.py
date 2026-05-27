from django.contrib import admin
from .models import LeadCapture


@admin.register(LeadCapture)
class LeadCaptureAdmin(admin.ModelAdmin):
    list_display = ('email', 'resource', 'created_at')
    list_filter = ('resource', 'created_at')
    search_fields = ('email',)
    readonly_fields = ('created_at',)
