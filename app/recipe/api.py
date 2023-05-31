
from .dto import RecipeDto, IngredientDto
from .services import RecipeService


class RecipeApi:

    @staticmethod
    def get_all_recipes():
        recipes = RecipeService.get_all_recipes()
        recipes_dtos = []

        for recipe in recipes:
            ingredients = RecipeService.get_ingredients(recipe.pk)
            recipes_dtos.append(RecipeApi.buid_recipe_dto(recipe, ingredients))

        return recipes_dtos

    @staticmethod
    def get_recipe(recipe_pk):
        recipe, ingredients = RecipeService.get_recipe(recipe_pk)
        return RecipeApi.buid_recipe_dto(recipe, ingredients)

    @staticmethod
    def create_recipe(validated_data):
        RecipeService.create_recipe(validated_data)
        print("validated_data" ,validated_data)

    @staticmethod
    def update_recipe(pk, serializer):
        RecipeService.update_recipe(pk, serializer)
        return RecipeApi.get_recipe(pk)

    @staticmethod
    def delete_recipe(recipe_pk):
        RecipeService.delete_recipe(recipe_pk)

    @staticmethod
    def buid_recipe_dto(recipe, ingredients):
        ingredients_dtos = [IngredientDto(
            name=ingredient.name) for ingredient in ingredients]

        recipe_dto = RecipeDto(
            id=recipe.id,
            name=recipe.name,
            description=recipe.description,
            ingredients=ingredients_dtos
        )
        return recipe_dto
