from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Menu
from .serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a few instances of the Menu model for testing
        Menu.objects.create(Title="Item 1", Price=10.0, Inventory=5)
        Menu.objects.create(Title="Item 2", Price=12.0, Inventory=3)
        Menu.objects.create(Title="Item 3", Price=8.0, Inventory=2)

    def test_getall(self):
        # Initialize the Django REST framework test client
        client = APIClient()

        # Define the URL to retrieve all Menu items
        url = reverse("menu-list")

        # Send a GET request to the URL
        response = client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Serialize the Menu instances and compare with the response data
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
