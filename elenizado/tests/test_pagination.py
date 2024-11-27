from django.test import TestCase
from django.urls import reverse
from elenizado.models import Publication, Categorie

class PaginationTestCase(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(nom="Science", description="Catégorie scientifique")
        for i in range(10):
            Publication.objects.create(
                titre=f"Publication {i}",
                description="Description test",
                categorie=self.categorie,
                image="img/adbox160x600.png"
            )
    
    def test_pagination_timeline(self):
        response = self.client.get(reverse("timeline"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["pub"]), 4)  # 4 éléments par page
