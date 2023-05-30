
from .models import Recipe, Ingredient
from .dto import RecipeDto, IngredientDto


class RecipeService:
    # Tk backend ref: services.py - get_users_by_cost_center_id  (line 452)
    @staticmethod
    def _get_ingredients(recipe_pk):
        ingredients = Ingredient.objects.filter(recipe=recipe_pk)
        ingredients_dtos = [IngredientDto(
            name=ingredient.name) for ingredient in ingredients]
        return ingredients_dtos

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
                    id=recipe.id,
                    name=recipe.name,
                    description=recipe.description,
                    ingredients=ingredients_dtos
                )
            )
        # return [RecipeDto.from_orm(recipe) for recipe in recipes]
        return recipe_dtos

    @staticmethod
    def get_recipe(recipe_pk):
        # ingredients=Ingredient.objects.filter(recipe=recipe.pk)
        # ingredients_dtos=[IngredientDto(name=ingredient.name) for ingredient in ingredients]
        recipe = Recipe.objects.get(pk=recipe_pk)
        ingredients_dtos = RecipeService._get_ingredients(recipe_pk)
        return RecipeDto(
            id=recipe.id,
            name=recipe.name,
            description=recipe.description,
            ingredients=ingredients_dtos
        )

    @staticmethod
    def delete_recipe(recipe_pk):
        recipe = Recipe.objects.get(pk=recipe_pk)  # or call get_recipe instead? nah!
        recipe.delete()

    @staticmethod
    def create_recipe(validated_data):
        ingredients_data = validated_data.pop('ingredients', None)
        recipe = Recipe.objects.create(**validated_data)

        if ingredients_data is not None:
            for ingredient_data in ingredients_data:
                print('hi from if ingredinet')
                Ingredient.objects.create(recipe=recipe, **ingredient_data)

        recipe_dto = RecipeService.get_recipe(recipe.pk)

        return recipe_dto

    @staticmethod
    def update_recipe(recipe_pk, validated_data):
        recipe = Recipe.objects.get(pk=recipe_pk)
        ingredients_data = validated_data.pop('ingredients', None)

        if ingredients_data is not None:
            recipe.ingredients.all().delete()
            for ingredient_data in ingredients_data:
                Ingredient.objects.create(recipe=recipe, **ingredient_data)

        for attr, value in validated_data.items():
            setattr(recipe, attr, value)

        recipe.save()
        recipe_dto = RecipeService.get_recipe(recipe_pk)

        return recipe_dto
