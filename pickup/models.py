from django.db import models
from donation.models import Donation
from volunteer.models import VolunteerProfile

class Pickup(models.Model):
    STATUS_CHOICES = (
        ('assigned', 'Assigned'),
        ('collected', 'Collected'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )
    donation = models.OneToOneField(Donation, on_delete=models.CASCADE, related_name='pickup_request')
    volunteer = models.ForeignKey(VolunteerProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='pickups')
    assigned_at = models.DateTimeField(auto_now_add=True)
    collected_at = models.DateTimeField(blank=True, null=True)
    delivered_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='assigned')

    def __str__(self):
        return f"Pickup for Donation {self.donation.id} by {self.volunteer.user.username if self.volunteer else 'Unassigned'}"
