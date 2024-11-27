from django.test import TestCase
from website.models import Newsletter
from django.urls import reverse

class NewsletterViewTest(TestCase):
    def setUp(self):
        """Initialisation des données nécessaires pour la newsletter."""
        self.newsletter_data = {
            'email': 'testnewsletter@example.com'
        }

    def test_is_newsletter_valid_email(self):
        """Vérifier la fonctionnalité d'inscription à la newsletter avec un email valide."""
        response = self.client.post(reverse('is_newsletter'), self.newsletter_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], "l'enregistrement a bien été effectué")
        self.assertTrue(Newsletter.objects.filter(email=self.newsletter_data['email']).exists())

    def test_is_newsletter_invalid_email(self):
        """Vérifier l'inscription à la newsletter avec un email invalide."""
        invalid_data = {
            'email': 'invalid-email'
        }
        response = self.client.post(reverse('is_newsletter'), invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], "email incorrect")
        self.assertFalse(Newsletter.objects.filter(email=invalid_data['email']).exists())
