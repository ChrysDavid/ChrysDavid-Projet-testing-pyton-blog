from django.test import TestCase
from django.urls import reverse
from elenizado import models

class ViewsTestCase(TestCase):
    def setUp(self):
        self.categorie = models.Categorie.objects.create(nom="Science", description="Catégorie scientifique")
        self.publication = models.Publication.objects.create(
            titre="Nouvelle découverte",
            description="Description de la découverte",
            categorie=self.categorie,
            image="image.jpg"
        )
    
    def test_timeline_view(self):
        response = self.client.get(reverse("timeline"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/list-two-column.html")
    
    def test_detail_view(self):
        response = self.client.get(reverse("detail", args=[self.publication.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/detail-standart.html")
    
    def test_cours_view(self):
        response = self.client.get(reverse("cours"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/cours.html")
