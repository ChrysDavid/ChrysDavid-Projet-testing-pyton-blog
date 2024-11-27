from django.core.paginator import Paginator
from django.test import TestCase
from django.urls import reverse
from website.models import SiteInfo
from elenizado.models import Publication

class PaginationTest(TestCase):
    def setUp(self):
        """Créer plusieurs publications pour tester la pagination."""
        self.site_info = SiteInfo.objects.create(
            email="contact@site.com",
            nom="Mon Site",
            telephone=123456789,
            description="Description du site",
            logo="logo.png"
        )
        for i in range(10):  # Créer 10 publications pour tester la pagination
            Publication.objects.create(
                titre=f"Publication {i+1}",
                description=f"Description de la publication {i+1}"
            )

    def test_index_pagination(self):
        """Vérifier que la pagination fonctionne correctement sur la page de l'index."""
        response = self.client.get(reverse('index') + '?page=1')
        paginator = Paginator(Publication.objects.all(), 4)  # 4 publications par page
        self.assertEqual(len(response.context['pub']), 4)
        self.assertEqual(response.status_code, 200)
