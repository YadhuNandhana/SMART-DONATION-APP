from django.db import models
from donor.models import User
from ngo.models import NGOProfile

class Donation(models.Model):
    CATEGORY_CHOICES = (
        ('food', 'Food'),
        ('clothing', 'Clothing'),
        ('electronics', 'Electronics'),
        ('books', 'Books'),
        ('other', 'Other'),
    )
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('matched', 'Matched'),
        ('picked_up', 'Picked Up'),
        ('delivered', 'Delivered'),
        ('rejected', 'Rejected'),
    )

    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donations')
    ngo = models.ForeignKey(NGOProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='received_donations')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    item_name = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    pickup_location = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Donation by {self.donor.username} - {self.item_name or self.category}"
