from django.test import TestCase
from django.urls import reverse
from website.models import SiteInfo
from elenizado.models import Publication, Evenement
from about.models import Gallerie

class IndexViewTest(TestCase):
    def setUp(self):
        """Initialiser les données pour les tests."""
        self.site_info = SiteInfo.objects.create(
            email="contact@site.com",
            nom="Mon Site",
            telephone=123456789,
            description="Description du site",
            logo="logo.png"
        )
        self.publication = Publication.objects.create(
            titre="Nouvelle Publication",
            description="Description de la publication"
        )
        self.evenement = Evenement.objects.create(
            titre="Événement Test",
            description="Description de l'événement"
        )
        self.gallerie = Gallerie.objects.create(
            titre="Image Test",
            gallerie="image.jpg"
        )

    def test_index_view_status_code(self):
        """Vérifier que la vue de l'index retourne un code de statut 200."""
        response = self.client.get(reverse('index'))  # Assurez-vous que 'index' correspond à l'URL
        self.assertEqual(response.status_code, 200)

    def test_index_view_template(self):
        """Vérifier que le bon template est utilisé."""
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, "pages/index.html")

    def test_index_view_context(self):
        """Vérifier que le contexte contient les bonnes données."""
        response = self.client.get(reverse('index'))
        self.assertIn('site_info', response.context)
        self.assertIn('publication_r', response.context)
        self.assertIn('events_r', response.context)
        self.assertIn('gallerie', response.context)

    def test_index_view_pagination(self):
        """Vérifier que la pagination fonctionne correctement sur la page de l'index."""
        response = self.client.get(reverse('index') + '?page=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('pub', response.context)  # Vérifier que la clé 'pub' contient des publications
