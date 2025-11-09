from rest_framework import serializers
from .models import NGOVerification
from ngo.serializers import NGOProfileSerializer
from donor.serializers import UserSerializer

class NGOVerificationSerializer(serializers.ModelSerializer):
    ngo = NGOProfileSerializer(read_only=True)
    verified_by = UserSerializer(read_only=True)

    class Meta:
        model = NGOVerification
        fields = '__all__'
