from django.test import TestCase

# Create your tests here.
from restaurant.models import Menu, Booking


#TestCase class
class test_booking(TestCase):
    def test_booking_str_representation(self):
        booking = Booking(name="John Doe", No_of_guests=4, BookingDate="2023-01-01 12:00:00")
        self.assertEqual(str(booking), "John Doe : 4 : 2023-01-01 12:00:00")



class test_menu(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="Ice Cream", price=8.0, inventory=100)
        self.assertEqual(item, "Ice Cream : 80")