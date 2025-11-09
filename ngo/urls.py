from django.urls import path
from .views import NGOProfileListCreateView, NGOProfileRetrieveUpdateDestroyView, NGONeedsListCreateView, NGONeedsRetrieveUpdateDestroyView

urlpatterns = [
    path('profiles/', NGOProfileListCreateView.as_view(), name='ngo_profile_list_create'),
    path('profiles/me/', NGOProfileRetrieveUpdateDestroyView.as_view(), name='ngo_profile_me'),
    path('profiles/<int:pk>/', NGOProfileRetrieveUpdateDestroyView.as_view(), name='ngo_profile_detail'),
    path('needs/', NGONeedsListCreateView.as_view(), name='ngo_needs_list_create'),
    path('needs/<int:pk>/', NGONeedsRetrieveUpdateDestroyView.as_view(), name='ngo_needs_detail'),
]
