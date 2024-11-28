from django.test import TestCase
from .models import Kullanici

class KullaniciModelTestCase(TestCase):
    def setUp(self):
        self.kullanici = Kullanici.objects.create(username="testuser", email="test@example.com")

    def test_kullanici_str(self):
        self.assertEqual(str(self.kullanici), "testuser")
