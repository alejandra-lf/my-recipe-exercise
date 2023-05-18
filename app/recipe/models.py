"""
Database models.
"""
from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    # display an instance of the model when necessary
    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return self.name
