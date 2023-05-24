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
        """Create recipe"""
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredient_data)
        return recipe

    def update(self, instance, validated_data):
        """Update recipe ingredients"""
        ingredients_data = validated_data.pop('ingredients', [])
        instance = super().update(instance, validated_data)

        if ingredients_data:
            instance.ingredients.all().delete()  # Remove existing ingredients

            for ingredient_data in ingredients_data:
                Ingredient.objects.create(recipe=instance, **ingredient_data) # New ingredients

            return instance

        else:
            raise serializers.ValidationError("No ingredients provided. Recipe not updated")

