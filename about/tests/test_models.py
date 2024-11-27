from django.test import TestCase
from about.models import Contact

class ContactModelTests(TestCase):
    def test_valid_contact_creation(self):
        """Test de création d'un contact avec des données valides."""
        contact = Contact.objects.create(
            nom="Alice",
            email="alice@example.com",
            subject="Sujet Test",
            telephone="123456789",
            message="Ceci est un message."
        )
        self.assertEqual(contact.nom, "Alice")
        self.assertTrue(contact.status)

    def test_invalid_contact_email(self):
        """Test de création d'un contact avec un email invalide."""
        with self.assertRaises(ValueError):
            Contact.objects.create(
                nom="Alice",
                email="email_invalid",
                subject="Sujet Test",
                telephone="123456789",
                message="Ceci est un message."
            )

    def test_edge_case_contact_fields(self):
        """Test des cas limites pour les champs du modèle."""
        long_name = "A" * 256  # Dépassement de la limite de longueur
        with self.assertRaises(ValueError):
            Contact.objects.create(
                nom=long_name,
                email="alice@example.com",
                subject="Sujet Test",
                telephone="123456789",
                message="Ceci est un message."
            )
