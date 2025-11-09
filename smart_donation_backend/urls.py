"""
URL configuration for smart_donation_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from donation.views import DonationListCreateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/donor/', include('donor.urls')),
    path('api/ngo/', include('ngo.urls')),
    path('api/volunteer/', include('volunteer.urls')),
    path('api/donations/', include('donation.urls')),
    path('api/pickups/', include('pickup.urls')),
    path('api/verification/', include('verification.urls')),
]
