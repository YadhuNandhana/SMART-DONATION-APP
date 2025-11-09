from django.db import models
from donor.models import User

class VolunteerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    badges = models.JSONField(default=list, blank=True, null=True) # e.g., ['Eco Warrior', 'Community Hero']
    points = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return self.user.username
