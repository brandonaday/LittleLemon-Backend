"""littlelemon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from restaurant import views

# Create a DefaultRouter for the BookingViewSet
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),  # Admin URL for managing the site
    path('restaurant/', include('restaurant.urls'), name='restaurant'),  # Include restaurant app URLs for restaurant-related views
    path('restaurant/menu/',include('restaurant.urls'), name='menu'),

    # Include BooskingViewSet URLs for table reservations
    path('restaurant/booking/', include(router.urls)),

    # Include authentication URLs for user management
    path('auth/', include('djoser.urls'), name='auth'),  
    path('auth/', include('djoser.urls.authtoken'), name='auth'),  

]