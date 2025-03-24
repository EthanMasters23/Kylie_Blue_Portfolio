from django.test import TestCase
from .models import Booking, Contact

class BookingModelTest(TestCase):
    def setUp(self):
        Booking.objects.create(name="Test User", email="test@example.com", phone="1234567890", date="2025-03-06", session_type="Photography", details="Test details")

    def test_booking_creation(self):
        booking = Booking.objects.get(name="Test User")
        self.assertEqual(booking.email, "test@example.com")

class ContactModelTest(TestCase):
    def setUp(self):
        Contact.objects.create(name="Test User", email="test@example.com", message="Test message")

    def test_contact_creation(self):
        contact = Contact.objects.get(name="Test User")
        self.assertEqual(contact.email, "test@example.com")
