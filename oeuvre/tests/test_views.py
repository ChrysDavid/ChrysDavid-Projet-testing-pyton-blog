from django.test import TestCase
from django.urls import reverse
from oeuvre.models import Poesie
from elenizado.models import Evenement
from about.models import Gallerie
from django.core.paginator import Paginator

class PoemeViewTest(TestCase):
    def setUp(self):
        """Préparer les données nécessaires pour les tests."""
        self.event1 = Evenement.objects.create(
            titre="Événement 1",
            description="Description de l'événement",
            image="event1.jpg"
        )
        self.gallerie1 = Gallerie.objects.create(
            titre="Image 1",
            gallerie="gallery1.jpg"
        )
        self.poesie1 = Poesie.objects.create(
            titre="Poème 1",
            description="Description du poème",
            poeme="<p>Ceci est un poème.</p>"
        )

    def test_poeme_view_status_code(self):
        """Vérifier que la vue retourne un statut HTTP 200."""
        response = self.client.get(reverse('poeme'))  # Assurez-vous que 'poeme' correspond au nom de l'URL.
        self.assertEqual(response.status_code, 200)

    def test_poeme_view_template_used(self):
        """Vérifier que le bon template est utilisé."""
        response = self.client.get(reverse('poeme'))
        self.assertTemplateUsed(response, "pages/poesie.html")

    def test_poeme_view_context(self):
        """Vérifier que le contexte contient les bonnes données."""
        response = self.client.get(reverse('poeme'))
        self.assertIn('poeme', response.context)
        self.assertIn('events_r', response.context)
        self.assertIn('gallerie', response.context)
        self.assertEqual(len(response.context['poeme']), 1)  # 1 poésie créée



        

class PoemePaginationTest(TestCase):
    def setUp(self):
        """Créer plusieurs poèmes pour tester la pagination."""
        for i in range(10):
            Poesie.objects.create(
                titre=f"Poème {i+1}",
                description="Description du poème",
                poeme="<p>Poème avec pagination.</p>"
            )

    def test_poeme_pagination(self):
        """Vérifier que la pagination fonctionne correctement."""
        response = self.client.get(reverse('poeme') + '?page=1')
        paginator = Paginator(Poesie.objects.filter(status=True), 4)  # Par exemple 4 par page
        self.assertEqual(len(response.context['poeme']), 4)
        self.assertEqual(response.status_code, 200)

