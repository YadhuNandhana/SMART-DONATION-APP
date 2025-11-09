from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import NGOVerification
from .serializers import NGOVerificationSerializer
from smart_donation_backend.permissions import IsAdmin, IsNGO

class NGOVerificationListCreateView(generics.ListCreateAPIView):
    serializer_class = NGOVerificationSerializer
    permission_classes = [IsAuthenticated, IsAdmin | IsNGO]

    def get_queryset(self):
        if self.request.user.role == 'ngo':
            return NGOVerification.objects.filter(ngo__user=self.request.user)
        elif self.request.user.is_staff:
            return NGOVerification.objects.all()
        return NGOVerification.objects.none()

    def perform_create(self, serializer):
        if self.request.user.role == 'ngo':
            ngo_profile = self.request.user.ngoprofile
            serializer.save(ngo=ngo_profile, darpan_id_submitted=self.request.data.get('darpan_id_submitted'), documents_submitted=True)
        else:
            serializer.save() # Admin can create for any NGO

class NGOVerificationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NGOVerification.objects.all()
    serializer_class = NGOVerificationSerializer
    permission_classes = [IsAuthenticated, IsAdmin | IsNGO]

    def get_queryset(self):
        if self.request.user.role == 'ngo':
            return NGOVerification.objects.filter(ngo__user=self.request.user)
        elif self.request.user.is_staff:
            return NGOVerification.objects.all()
        return NGOVerification.objects.none()

    def perform_update(self, serializer):
        if self.request.user.is_staff and 'is_approved' in self.request.data:
            serializer.save(verified_by=self.request.user, approved_at=timezone.now())
        else:
            serializer.save()
