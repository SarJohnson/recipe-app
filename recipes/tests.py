from django.test import TestCase
from .models import Recipe
from .forms import RecipeSearchForm

class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(name='Tea', ingredients='Tea leaves, Water, Sugar', cooking_time=10, description='test description')
    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/list/1')

class RecipeSearchFormTest(TestCase):
    def test_form_renders_recipe_diff_input(self):
        form = RecipeSearchForm()
        self.assertIn('recipe_diff', form.as_p())
    def test_form_renders_chart_type_input(self):
        form = RecipeSearchForm()
        self.assertIn('chart_type', form.as_p())
    def test_form_valid_data(self):
        form = RecipeSearchForm(
            data={'recipe_diff': '#1', 'chart_type': '#2'})
        self.assertTrue(form.is_valid())
    def test_form_invalid_data(self):
        form = RecipeSearchForm(data={'recipe_diff': '', 'chart_type': ''})
        self.assertFalse(form.is_valid())