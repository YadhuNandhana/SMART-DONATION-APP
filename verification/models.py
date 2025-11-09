from django.db import models
from ngo.models import NGOProfile
from donor.models import User

class NGOVerification(models.Model):
    ngo = models.OneToOneField(NGOProfile, on_delete=models.CASCADE, related_name='verification')
    darpan_id_submitted = models.CharField(max_length=50, blank=True, null=True)
    documents_submitted = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='ngo_verifications')
    submitted_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Verification for {self.ngo.ngo_name} - {'Approved' if self.is_approved else 'Pending'}"
