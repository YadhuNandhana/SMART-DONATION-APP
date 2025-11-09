from rest_framework import serializers
from .models import Pickup
from donation.serializers import DonationSerializer
from volunteer.serializers import VolunteerProfileSerializer

class PickupSerializer(serializers.ModelSerializer):
    donation = DonationSerializer(read_only=True)
    volunteer = VolunteerProfileSerializer(read_only=True)

    class Meta:
        model = Pickup
        fields = '__all__'
