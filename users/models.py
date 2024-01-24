from django.db import models
from recipes.models import Recipe

class User(models.Model):
    name = models.CharField(max_length=120)
    saved_recipes = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    def _str_(self):
        return f" {self.name}, saved recipes: {self.saved_recipes.name}"
