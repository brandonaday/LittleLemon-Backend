from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Booking(models.Model):
    """
    Represents a restaurant reservation.
    """
    name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(default=1, help_text="Number of guests in the reservation")
    BookingDate = models.DateTimeField(default=None, help_text="Date and time of the reservation", null=True)

    def __str__(self):
        return f'{self.name} : {str(self.No_of_guests)}  : {str(self.BookingDate)}'

class Menu(models.Model):
    """
    Represents a menu item offered by the restaurant.
    """
    Title = models.CharField(max_length=255, help_text="Name of the menu item")
    Price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the menu item", default=None)
    Inventory = models.IntegerField(default=0, validators=[MaxValueValidator(limit_value=5)]  # Set the maximum value to 99999
, help_text="Available quantity of the menu item")

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'