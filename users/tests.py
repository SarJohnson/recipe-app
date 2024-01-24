from django.test import TestCase
from .models import User, Recipe

class UserModelTest(TestCase):
    def setUpTestData():
        recipe = Recipe.objects.create(name='tea', cooking_time=5, difficulty='easy', ingredients='water, sugar, leaves', description='boil water, then add tea leaves, finally add sugar to taste')
        recipe.save()
        user = User.objects.create(name='Sarah', saved_recipes = recipe)
        user.save()
    def test_user_name(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('saved_recipes').verbose_name
        self.assertEqual(field_label, 'saved recipes')
