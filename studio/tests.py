from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Fitness, Booking

class BookingAPITestCase(APITestCase):
    """
    Unit tests for Booking API:
    - Booking success
    - Overbooking
    - Duplicate prevention
    - Class listing and filtering
    """
    def setUp(self):
        self.fitness = Fitness.objects.create(
            name="Yoga",
            datetime="2025-06-26T07:00:00Z",
            instructor="Rina",
            available_slots=1
        )
        self.booking_data = {
            "fitness_class": self.fitness.id,
            "client_name": "John",
            "client_email": "john@example.com"
        }

    def test_get_classes(self):
        response = self.client.get("/api/classes-list/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

    def test_successful_booking(self):
        response = self.client.post("/api/book-class/", self.booking_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_overbooking(self):
        self.client.post("/api/book-class/", self.booking_data, format='json')
        second_booking = {
            "fitness_class": self.fitness.id,
            "client_name": "Jane",
            "client_email": "jane@example.com"
        }
        response = self.client.post("/api/book-class/", second_booking, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("No slots left", str(response.content))

    def test_get_bookings_by_email(self):
        self.client.post("/api/book-class/", self.booking_data, format='json')
        response = self.client.get('/api/my-bookings/?email=john@example.com')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['client_email'], "john@example.com")

    def test_duplicate_booking(self):
        fitness = Fitness.objects.create(
            name="Pilates",
            datetime="2025-06-27T07:00:00Z",
            instructor="Jane",
            available_slots=2
        )
        booking_data = {
            "fitness_class": fitness.id,
            "client_name": "John",
            "client_email": "john@example.com"
        }
        self.client.post("/api/book-class/", booking_data, format='json')
        response = self.client.post("/api/book-class/", booking_data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("already booked", str(response.content))
