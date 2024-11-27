from django.test import TestCase
from django.urls import reverse
from oeuvre.models import Poesie
from elenizado.models import Evenement
from about.models import Gallerie

class PoemeIntegrationTest(TestCase):
    def setUp(self):
        """Initialisation des données nécessaires."""
        self.event = Evenement.objects.create(
            titre="Événement Test",
            description="Description de test",
            image="event.jpg"
        )
        self.gallerie = Gallerie.objects.create(
            titre="Gallerie Test",
            gallerie="image.jpg"
        )
        self.poesie = Poesie.objects.create(
            titre="Poésie Test",
            description="Description du poème",
            poeme="<p>Poème pour test.</p>"
        )

    def test_poesie_with_events_and_gallerie(self):
        """Vérifier l'intégration entre les poèmes, événements et galeries."""
        response = self.client.get(reverse('poeme'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.event.titre)
        self.assertContains(response, self.gallerie.titre)
        self.assertContains(response, self.poesie.titre)
