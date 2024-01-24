from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length = 120)
    cooking_time = models.IntegerField(help_text = 'in minutes', default = 0)
    ingredients = models.CharField(max_length = 500)
    difficulty = models.CharField(max_length = 30)
    description = models.TextField()

    def _str_(self):
        return str(self.name)
