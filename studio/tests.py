from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Fitness, Booking

# Create your tests here.
class BookingAPITestCase(TestCase):
    """
    Unit tests for Booking API:
    - Booking success
    - Overbooking
    - Duplicate prevention
    - Class listing and filtering
    """
    def setUp(self):
        self.client = APIClient()
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
        response = self.client.get("/api/classes/")
        self.assertEqual(response.status_code,200)
        self.assertTrue(len(response.data)>0)

    def test_successful_booking(self):
        response = self.client.post("/api/book/",self.booking_data,format = 'json')
        self.assertEqual(response.status_code,201)

    def test_overbooking(self):
        self.client.post("/api/book/",self.booking_data,format = 'json')
        second_booking = {
        "fitness_class": self.fitness.id,
        "client_name": "Jane",
        "client_email": "jane@example.com"  # ✅ Different email avoids duplicate check
        }
        response = self.client.post("/api/book/",second_booking,format = 'json')
        self.assertEqual(response.status_code,400)
        self.assertIn("No slots left for this class.",str(response.data))

    def test_get_bookings_by_email(self):
        self.client.post("/api/book/",self.booking_data,format = 'json')
        response = self.client.get('/api/bookings/',{'email':'john@example.com'})
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data[0]['client_email'],"john@example.com")

    def test_duplicate_booking(self):
        fitness = Fitness.objects.create(
        name="Pilates",
        datetime="2025-06-27T07:00:00Z",
        instructor="Jane",
        available_slots=2  # ✅ enough for two bookings
        )

        booking_data = {
        "fitness_class": fitness.id,
        "client_name": "John",
        "client_email": "john@example.com"
        }
        self.client.post("/api/book/", self.booking_data, format='json')
        response = self.client.post("/api/book/", self.booking_data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("You have already booked this class.", str(response.data))