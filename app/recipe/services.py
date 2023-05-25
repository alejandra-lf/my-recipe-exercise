"""
Similar to
def get_users_by_cost_center_id  (line 452)
from services.py
"""

from .models import Recipe, Ingredient
from .dto import RecipeDto, IngredientDto


class RecipeService:

    @staticmethod
    def get_all_recipes():
        recipes = Recipe.objects.all()

        recipe_dtos = []

        for recipe in recipes:
            # ingredients=Ingredient.objects.filter(recipe=recipe.pk)
            # ingredients_dtos=[IngredientDto(name=ingredient.name) for ingredient in ingredients]
            ingredients_dtos = RecipeService._get_ingredients(recipe.pk)

            recipe_dtos.append(
                RecipeDto(
                    name=recipe.name,
                    description=recipe.description,
                    ingredients=ingredients_dtos
                )
            )
        # return [RecipeDto.from_orm(recipe) for recipe in recipes]
        return recipe_dtos

    @staticmethod
    def get_recipe(recipe_pk):
        recipe = Recipe.objects.get(pk=recipe_pk)
        ingredients_dtos = RecipeService._get_ingredients(recipe_pk)

        # ingredients=Ingredient.objects.filter(recipe=recipe.pk)
        # ingredients_dtos=[IngredientDto(name=ingredient.name) for ingredient in ingredients]

        return RecipeDto(
            name=recipe.name,
            description=recipe.description,
            ingredients=ingredients_dtos)

    @staticmethod
    def _get_ingredients(recipe_pk):
        ingredients = Ingredient.objects.filter(recipe=recipe_pk)
        ingredients_dtos = [IngredientDto(
            name=ingredient.name) for ingredient in ingredients]
        return ingredients_dtos
