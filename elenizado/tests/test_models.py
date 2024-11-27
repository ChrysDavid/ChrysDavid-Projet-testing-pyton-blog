from django.test import TestCase
from elenizado import models

class ModelsTestCase(TestCase):
    def setUp(self):
        self.categorie = models.Categorie.objects.create(nom="Science", description="Catégorie scientifique")
        self.publication = models.Publication.objects.create(
            titre="Nouvelle découverte",
            description="Description de la découverte",
            categorie=self.categorie,
            image="image.jpg"
        )
    
    def test_categorie_creation(self):
        self.assertEqual(self.categorie.nom, "Science")
    
    def test_publication_creation(self):
        self.assertEqual(self.publication.titre, "Nouvelle découverte")
        self.assertIsNotNone(self.publication.slug)
