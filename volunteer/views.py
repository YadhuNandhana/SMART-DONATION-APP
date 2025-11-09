from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import VolunteerProfile
from .serializers import VolunteerProfileSerializer
from smart_donation_backend.permissions import IsVolunteer, IsAdmin

class VolunteerProfileListCreateView(generics.ListCreateAPIView):
    queryset = VolunteerProfile.objects.all()
    serializer_class = VolunteerProfileSerializer
    permission_classes = [IsAuthenticated] # Anyone can register as a volunteer

class VolunteerProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VolunteerProfile.objects.all()
    serializer_class = VolunteerProfileSerializer
    permission_classes = [IsAuthenticated, IsVolunteer | IsAdmin]

    def get_object(self):
        if self.request.user.role == 'volunteer':
            return self.request.user.volunteerprofile
        return super().get_object()
