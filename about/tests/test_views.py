from django.urls import reverse
from django.test import TestCase
from about.models import Contact

class ContactViewTests(TestCase):
    def test_valid_contact_submission(self):
        """Test de soumission avec des données valides."""
        data = {
            "name": "Alice",
            "email": "alice@example.com",
            "subject": "Sujet Test",
            "tel": "123456789",
            "messages": "Message Test"
        }
        response = self.client.post(reverse('is_contact'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Contact.objects.filter(email="alice@example.com").exists())

    def test_invalid_contact_email_submission(self):
        """Test de soumission avec un email invalide."""
        data = {
            "name": "Alice",
            "email": "invalid-email",
            "subject": "Sujet Test",
            "tel": "123456789",
            "messages": "Message Test"
        }
        response = self.client.post(reverse('is_contact'), data)
        self.assertEqual(response.status_code, 400)  # Mauvaise requête
        self.assertIn("email incorrect", response.json().get("message", ""))

    def test_missing_fields_submission(self):
        """Test de soumission avec des champs manquants."""
        data = {
            "name": "Alice",
            "email": "alice@example.com"
        }
        response = self.client.post(reverse('is_contact'), data)
        self.assertEqual(response.status_code, 400)
        self.assertFalse(Contact.objects.filter(email="alice@example.com").exists())
