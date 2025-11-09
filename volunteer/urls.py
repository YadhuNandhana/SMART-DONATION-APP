from django.urls import path
from .views import VolunteerProfileListCreateView, VolunteerProfileRetrieveUpdateDestroyView

urlpatterns = [
    path('profiles/', VolunteerProfileListCreateView.as_view(), name='volunteer_profile_list_create'),
    path('profiles/me/', VolunteerProfileRetrieveUpdateDestroyView.as_view(), name='volunteer_profile_me'),
    path('profiles/<int:pk>/', VolunteerProfileRetrieveUpdateDestroyView.as_view(), name='volunteer_profile_detail'),
]
