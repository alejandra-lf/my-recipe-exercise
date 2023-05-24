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
        return [RecipeDto.from_orm(recipe) for recipe in recipes]
