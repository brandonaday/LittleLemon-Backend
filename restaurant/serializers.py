from rest_framework import serializers
from .models import Menu, Booking
from django.contrib.auth.models import User

class MenuSerializer(serializers.ModelSerializer):
    """
    Serializer for the Menu model.
    """

    class Meta:
        model = Menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    """

    class Meta:
        model = Booking
        fields = '__all__'

#define Serializer class for User model
class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for User model
    """
    
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']