from django.test import TestCase
from oeuvre.models import Poesie

class PoesieModelTest(TestCase):
    def setUp(self):
        """Initialisation des données de test."""
        self.poesie = Poesie.objects.create(
            titre="Poème d'Automne",
            description="Un poème sur l'automne",
            poeme="<p>Ceci est un poème.</p>"
        )

    def test_poesie_creation(self):
        """Test de création d'une poésie avec des données valides."""
        self.assertEqual(self.poesie.titre, "Poème d'Automne")
        self.assertEqual(self.poesie.description, "Un poème sur l'automne")
        self.assertTrue(self.poesie.status)

    def test_poesie_str_method(self):
        """Test de la méthode __str__."""
        self.assertEqual(str(self.poesie), "Poème d'Automne")

    def test_poesie_default_status(self):
        """Test que le statut par défaut est actif (True)."""
        poesie = Poesie.objects.create(
            titre="Poème inactif",
            description="Un poème désactivé",
            poeme="<p>Poème désactivé.</p>",
            status=False
        )
        self.assertFalse(poesie.status)
