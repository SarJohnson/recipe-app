from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(name='tea', cooking_time=5, difficulty='easy', ingredients='water, sugar, leaves', description='boil water, then add tea leaves, finally add sugar to taste')
    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/list/1')