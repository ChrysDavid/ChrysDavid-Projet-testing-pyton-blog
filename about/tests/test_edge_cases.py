from django.urls import reverse
from django.test import TestCase
from about.models import Contact


class ContactEdgeCaseTests(TestCase):
    def test_empty_field_submission(self):
        """Test avec des champs vides."""
        data = {
            "name": "",
            "email": "",
            "subject": "",
            "tel": "",
            "messages": ""
        }
        response = self.client.post(reverse('is_contact'), data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("champs obligatoires manquants", response.json().get("message", ""))

    def test_large_input_fields(self):
        """Test avec des entrées très longues."""
        data = {
            "name": "A" * 300,
            "email": "a" * 250 + "@example.com",
            "subject": "B" * 300,
            "tel": "1" * 50,
            "messages": "C" * 5000
        }
        response = self.client.post(reverse('is_contact'), data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("dépassement de longueur", response.json().get("message", ""))
