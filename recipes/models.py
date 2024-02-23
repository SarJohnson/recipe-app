from django.db import models
from django.shortcuts import reverse

class Recipe(models.Model):
    name = models.CharField(max_length = 120)
    cooking_time = models.IntegerField(help_text = 'in minutes', default = 0)
    ingredients = models.CharField(max_length = 500)
    description = models.TextField()
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def calc_difficulty(self):
        ingredients = self.ingredients.split(', ')
        if self.cooking_time <= 90 and len(ingredients) <= 5:
            difficulty = 'Easy'
        elif self.cooking_time <= 90 and len(ingredients) > 5:
            difficulty = 'Intermediate'
        elif self.cooking_time > 90 and len(ingredients) < 10:
            difficulty = 'Hard'
        elif self.cooking_time > 90 and len(ingredients) >= 10:
            difficulty = 'Expert'
        return difficulty

    def get_absolute_url(self):
        return reverse ('recipes:detail', kwargs={'pk': self.pk})

    def _str_(self):
        return str(self.name)
