from django.test import TestCase
from website.models import SiteInfo, SocialCount, Newsletter

class SiteInfoModelTest(TestCase):
    def setUp(self):
        self.site_info = SiteInfo.objects.create(
            email="contact@site.com",
            nom="Mon Site",
            telephone=123456789,
            description="Description du site",
            logo="site_logo.png"
        )

    def test_site_info_creation(self):
        """Vérifier la création du modèle SiteInfo."""
        self.assertEqual(self.site_info.nom, "Mon Site")
        self.assertTrue(self.site_info.status)

    def test_site_info_str_method(self):
        """Vérifier la méthode __str__ du modèle SiteInfo."""
        self.assertEqual(str(self.site_info), "Mon Site")

class SocialCountModelTest(TestCase):
    def setUp(self):
        self.social_count = SocialCount.objects.create(
            nom="Facebook",
            lien="https://facebook.com",
            icones="fa-facebook-f"
        )

    def test_social_count_creation(self):
        """Vérifier la création du modèle SocialCount."""
        self.assertEqual(self.social_count.nom, "Facebook")
        self.assertEqual(self.social_count.icones, "fa-facebook-f")

    def test_social_count_str_method(self):
        """Vérifier la méthode __str__ du modèle SocialCount."""
        self.assertEqual(str(self.social_count), "Facebook")

class NewsletterModelTest(TestCase):
    def setUp(self):
        self.newsletter = Newsletter.objects.create(
            email="test@example.com"
        )

    def test_newsletter_creation(self):
        """Vérifier la création du modèle Newsletter."""
        self.assertEqual(self.newsletter.email, "test@example.com")
        self.assertTrue(self.newsletter.status)

    def test_newsletter_str_method(self):
        """Vérifier la méthode __str__ du modèle Newsletter."""
        self.assertEqual(str(self.newsletter), "test@example.com")
