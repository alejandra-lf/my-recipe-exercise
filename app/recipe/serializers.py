"""
Serializers for recipe API
"""
from rest_framework import serializers

from .models import Recipe, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    # initialize model and fields to serialize
    class Meta:
        model = Ingredient
        fields = ['name']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = '__all__'

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredient_data)
        return recipe

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)