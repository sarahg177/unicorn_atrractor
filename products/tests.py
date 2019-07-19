from django.test import TestCase
from .models import Product


class ProductTests(TestCase):
    """Tests again Product model"""
    def test_str(self):
        test_name = Product(name='A Product')
        self.assertEqual(str(test_name), 'A Product')
