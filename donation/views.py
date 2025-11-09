from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Donation
from .serializers import DonationSerializer
from smart_donation_backend.permissions import IsDonor, IsNGO, IsAdmin
from smart_donation_backend.utils import find_nearest_ngos
from ngo.serializers import NGOProfileSerializer
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum, Count
from django.shortcuts import get_object_or_404
from ngo.models import NGOProfile
from donor.models import User

class DonationListCreateView(generics.ListCreateAPIView):
    serializer_class = DonationSerializer
    permission_classes = [IsAuthenticated, IsDonor | IsAdmin]

    def get_queryset(self):
        if self.request.user.role == 'donor':
            return Donation.objects.filter(donor=self.request.user)
        elif self.request.user.role == 'ngo':
            # NGOs can see donations matched to them or available donations
            return Donation.objects.filter(Q(ngo__user=self.request.user) | Q(status='pending'))
        elif self.request.user.is_staff: # Admin
            return Donation.objects.all()
        return Donation.objects.none()

    def perform_create(self, serializer):
        if self.request.user.role == 'donor':
            donation = serializer.save(donor=self.request.user)
            # Auto-suggest nearest NGOs
            if donation.latitude and donation.longitude:
                nearest_ngos = find_nearest_ngos(donation.latitude, donation.longitude)
                # For MVP, let's just assign the closest verified NGO if available
                if nearest_ngos:
                    donation.ngo = nearest_ngos[0]['ngo']
                    donation.status = 'matched'
                    donation.save()
        else:
            # Admin can create donations for any donor, assuming donor_id is provided in data
            serializer.save()

class DonationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [IsAuthenticated, IsDonor | IsAdmin]

    def get_queryset(self):
        if self.request.user.role == 'donor':
            return Donation.objects.filter(donor=self.request.user)
        elif self.request.user.is_staff:
            return Donation.objects.all()
        return Donation.objects.none()

    def perform_update(self, serializer):
        # Add logic for NGO to accept/reject donations
        if self.request.user.role == 'ngo' and self.get_object().ngo == self.request.user.ngoprofile:
            if 'status' in self.request.data:
                new_status = self.request.data['status']
                if new_status in ['matched', 'rejected']:
                    serializer.save(status=new_status)
                    return
        serializer.save()

class ExpiringDonationsView(generics.ListAPIView):
    serializer_class = DonationSerializer
    permission_classes = [IsAuthenticated, IsAdmin] # Only admin can view expiring donations

    def get_queryset(self):
        # Donations expiring in the next 3 days
        three_days_from_now = timezone.now().date() + timedelta(days=3)
        return Donation.objects.filter(expiry_date__lte=three_days_from_now, status='pending')

class NearestNGOsView(generics.RetrieveAPIView):
    serializer_class = NGOProfileSerializer
    permission_classes = [IsAuthenticated, IsDonor]

    def get(self, request, *args, **kwargs):
        donation_id = self.kwargs.get('pk')
        donation = get_object_or_404(Donation, id=donation_id, donor=request.user)

        if not donation.latitude or not donation.longitude:
            return Response({"detail": "Donation location not specified."}, status=status.HTTP_400_BAD_REQUEST)

        nearest_ngos = find_nearest_ngos(donation.latitude, donation.longitude)
        serializer = NGOProfileSerializer([item['ngo'] for item in nearest_ngos], many=True)
        return Response(serializer.data)

class AnalyticsDashboardView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request, *args, **kwargs):
        total_donations_count = Donation.objects.count()
        total_redistributed_items = Donation.objects.filter(status='delivered').aggregate(Sum('quantity'))['quantity__sum'] or 0
        
        donations_by_category = Donation.objects.values('category').annotate(count=Count('id'), total_quantity=Sum('quantity'))
        
        active_ngos_count = NGOProfile.objects.filter(is_verified=True).count()
        
        # Example: Donations over time (last 30 days)
        thirty_days_ago = timezone.now() - timedelta(days=30)
        donations_over_time = Donation.objects.filter(created_at__gte=thirty_days_ago).values('created_at__date').annotate(count=Count('id')).order_by('created_at__date')

        return Response({
            "total_donations_count": total_donations_count,
            "total_redistributed_items": total_redistributed_items,
            "donations_by_category": donations_by_category,
            "active_ngos_count": active_ngos_count,
            "donations_over_time": donations_over_time,
        })
