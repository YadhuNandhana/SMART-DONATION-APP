from django.urls import path
from .views import NGOVerificationListCreateView, NGOVerificationRetrieveUpdateDestroyView

urlpatterns = [
    path('', NGOVerificationListCreateView.as_view(), name='ngo_verification_list_create'),
    path('<int:pk>/', NGOVerificationRetrieveUpdateDestroyView.as_view(), name='ngo_verification_detail'),
]
