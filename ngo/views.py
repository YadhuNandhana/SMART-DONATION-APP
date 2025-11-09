from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import NGOProfile, NGONeeds
from .serializers import NGOProfileSerializer, NGONeedsSerializer
from smart_donation_backend.permissions import IsNGO, IsAdmin

class NGOProfileListCreateView(generics.ListCreateAPIView):
    queryset = NGOProfile.objects.all()
    serializer_class = NGOProfileSerializer
    permission_classes = [IsAuthenticated] # Anyone can register an NGO, verification is separate

class NGOProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NGOProfile.objects.all()
    serializer_class = NGOProfileSerializer
    permission_classes = [IsAuthenticated, IsNGO | IsAdmin] # Only NGO owner or admin can update/delete

    def get_object(self):
        # For NGO users, they can only access their own profile
        if self.request.user.role == 'ngo':
            return self.request.user.ngoprofile
        # For admin, they can access any NGO profile by pk
        return super().get_object()

class NGONeedsListCreateView(generics.ListCreateAPIView):
    serializer_class = NGONeedsSerializer
    permission_classes = [IsAuthenticated, IsNGO | IsAdmin]

    def get_queryset(self):
        if self.request.user.role == 'ngo':
            return NGONeeds.objects.filter(ngo__user=self.request.user)
        return NGONeeds.objects.all()

    def perform_create(self, serializer):
        if self.request.user.role == 'ngo':
            ngo_profile = NGOProfile.objects.get(user=self.request.user)
            serializer.save(ngo=ngo_profile)
        else:
            # Admin can create needs for any NGO, assuming ngo_id is provided in data
            serializer.save()

class NGONeedsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NGONeeds.objects.all()
    serializer_class = NGONeedsSerializer
    permission_classes = [IsAuthenticated, IsNGO | IsAdmin]

    def get_queryset(self):
        if self.request.user.role == 'ngo':
            return NGONeeds.objects.filter(ngo__user=self.request.user)
        return NGONeeds.objects.all()
