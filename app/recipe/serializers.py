"""
Serializers for recipe API
"""
from rest_framework import serializers

from .models import Recipe, Ingredient


class IngredientSerializer(serializers.Serializer):
    # initialize model and fields to serialize
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'recipe')


class RecipeSerializer(serializers.Serializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = '__all__' # another way
