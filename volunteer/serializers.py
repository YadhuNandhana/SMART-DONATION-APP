from rest_framework import serializers
from .models import VolunteerProfile
from donor.serializers import UserSerializer

class VolunteerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = VolunteerProfile
        fields = '__all__'
