from django.contrib import admin
from .models import JobApplication

# Register your models here.

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'applied_at', 'status')
    list_filter = ('status', 'applied_at')
    search_fields = ('first_name', 'last_name', 'email')
    actions = ['shortlist_applicants', 'reject_applicants']

    @admin.action(description="Shortlist selected applicants")
    def shortlist_applicants(self, request, queryset):
        queryset.update(status='shortlisted')

    @admin.action(description="Reject selected applicants")
    def reject_applicants(self, request, queryset):
        queryset.update(status='rejected')

admin.site.register(JobApplication, JobApplicationAdmin)
