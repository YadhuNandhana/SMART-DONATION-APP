from django.contrib import admin
from .models import NGOVerification

@admin.register(NGOVerification)
class NGOVerificationAdmin(admin.ModelAdmin):
    list_display = ('ngo', 'darpan_id_submitted', 'is_approved', 'verified_by', 'submitted_at', 'approved_at')
    list_filter = ('is_approved',)
    search_fields = ('ngo__ngo_name', 'darpan_id_submitted')
    actions = ['approve_ngos', 'reject_ngos']

    def approve_ngos(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, "Selected NGOs have been approved.")
    approve_ngos.short_description = "Approve selected NGOs"

    def reject_ngos(self, request, queryset):
        queryset.update(is_approved=False)
        self.message_user(request, "Selected NGOs have been rejected.")
    reject_ngos.short_description = "Reject selected NGOs"
