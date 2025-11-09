from rest_framework import serializers
from .models import User, DonorProfile
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role', 'phone_number', 'address', 'latitude', 'longitude', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'donor'),
            phone_number=validated_data.get('phone_number'),
            address=validated_data.get('address'),
            latitude=validated_data.get('latitude'),
            longitude=validated_data.get('longitude')
        )
        if user.role == 'donor':
            DonorProfile.objects.create(user=user)
        # Add similar logic for NGO and Volunteer profiles if they are created at user registration
        return user

class DonorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = DonorProfile
        fields = '__all__'
