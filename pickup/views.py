from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Pickup
from .serializers import PickupSerializer
from smart_donation_backend.permissions import IsVolunteer, IsAdmin

class PickupListCreateView(generics.ListCreateAPIView):
    serializer_class = PickupSerializer
    permission_classes = [IsAuthenticated, IsAdmin] # Only admin can create/list all pickups

    def get_queryset(self):
        if self.request.user.role == 'volunteer':
            return Pickup.objects.filter(volunteer__user=self.request.user)
        elif self.request.user.is_staff:
            return Pickup.objects.all()
        return Pickup.objects.none()

class PickupRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pickup.objects.all()
    serializer_class = PickupSerializer
    permission_classes = [IsAuthenticated, IsVolunteer | IsAdmin]

    def get_queryset(self):
        if self.request.user.role == 'volunteer':
            return Pickup.objects.filter(volunteer__user=self.request.user)
        elif self.request.user.is_staff:
            return Pickup.objects.all()
        return Pickup.objects.none()
