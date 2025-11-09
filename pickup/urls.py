from django.urls import path
from .views import PickupListCreateView, PickupRetrieveUpdateDestroyView

urlpatterns = [
    path('', PickupListCreateView.as_view(), name='pickup_list_create'),
    path('<int:pk>/', PickupRetrieveUpdateDestroyView.as_view(), name='pickup_detail'),
]
