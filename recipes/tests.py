from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from recipes.models import Recipe  # Ajuste o import conforme seus models

class RecipeModelTest(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(name="Bolo de Chocolate")

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.name, "Bolo de Chocolate")

class HomeViewTest(TestCase):
    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
