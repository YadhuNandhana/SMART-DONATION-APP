from django.urls import path
from .views import (
    DonationListCreateView,
    DonationRetrieveUpdateDestroyView,
    ExpiringDonationsView,
    NearestNGOsView,
    AnalyticsDashboardView,
)

urlpatterns = [
    path('', DonationListCreateView.as_view(), name='donation_list_create'),
    path('<int:pk>/', DonationRetrieveUpdateDestroyView.as_view(), name='donation_detail'),
    path('expiring/', ExpiringDonationsView.as_view(), name='expiring_donations'),
    path('<int:pk>/nearest-ngos/', NearestNGOsView.as_view(), name='nearest_ngos'),
    path('analytics/', AnalyticsDashboardView.as_view(), name='analytics_dashboard'),
]

