from rest_framework import serializers
from .models import NGOProfile, NGONeeds
from donor.serializers import UserSerializer

class NGOProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = NGOProfile
        fields = '__all__'

class NGONeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NGONeeds
        fields = '__all__'
