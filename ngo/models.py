from django.db import models
from donor.models import User

class NGOProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    ngo_name = models.CharField(max_length=255)
    darpan_id = models.CharField(max_length=50, unique=True, blank=True, null=True)
    fcra_details = models.CharField(max_length=255, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return self.ngo_name

class NGONeeds(models.Model):
    ngo = models.ForeignKey(NGOProfile, on_delete=models.CASCADE, related_name='needs')
    item_category = models.CharField(max_length=100)
    quantity_needed = models.IntegerField()
    urgency = models.CharField(max_length=20, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ngo.ngo_name} - {self.item_category} ({self.quantity_needed})"
