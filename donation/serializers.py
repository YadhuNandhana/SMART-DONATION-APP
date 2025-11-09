from rest_framework import serializers
from .models import Donation
from donor.serializers import UserSerializer
from ngo.serializers import NGOProfileSerializer

class DonationSerializer(serializers.ModelSerializer):
    donor = UserSerializer(read_only=True)
    ngo = NGOProfileSerializer(read_only=True)

    class Meta:
        model = Donation
        fields = '__all__'
