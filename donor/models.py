from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_ROLES = (
        ('donor', 'Donor'),
        ('ngo', 'NGO'),
        ('volunteer', 'Volunteer'),
    )
    role = models.CharField(max_length=10, choices=USER_ROLES, default='donor')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return self.username

class DonorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # Additional donor-specific fields can go here

    def __str__(self):
        return self.user.username
