from django.test import TestCase
from django.urls import reverse
from about.models import Contact

class IntegrationTests(TestCase):
    def test_contact_view_creates_model_instance(self):
        """Vérifie que la vue crée une instance dans la base de données."""
        data = {
            "name": "Alice",
            "email": "alice@example.com",
            "subject": "Sujet Test",
            "tel": "123456789",
            "messages": "Message Test"
        }
        response = self.client.post(reverse('is_contact'), data)
        self.assertEqual(response.status_code, 200)
        contact = Contact.objects.get(email="alice@example.com")
        self.assertEqual(contact.nom, "Alice")
