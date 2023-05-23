from django.test import TestCase
from recipe.serializers import RecipeSerializer

from recipe.models import Recipe, Ingredient


class RecipeTests(TestCase):

    def test_recipe_creation(self):
        # Mock request with the payload
        payload = {
            "name": "Pizza",
            "description": "Put it in the oven",
            "ingredients": [
                {"name": "dough"},
                {"name": "cheese"},
                {"name": "tomato"}
            ]
        }

        # Create a serializer instance and validate the payload
        serializer = RecipeSerializer(data=payload)
        self.assertTrue(serializer.is_valid())

        # Create the recipe by saving the serializer
        recipe = serializer.save()

        # Checking
        self.assertEqual(recipe.name, payload['name'])
        self.assertEqual(recipe.description, payload['description'])
        self.assertEqual(recipe.ingredients.count(), 3)

        # Using set comprehension (Tom's suggestion)  :D
        ingredient_names = {ingredient.name for ingredient in recipe.ingredients.all()}
        ingredient_names_payload = {ingredient['name'] for ingredient in payload['ingredients']}
        self.assertEqual(ingredient_names, ingredient_names_payload)

    def test_update_recipe_ingredients(self):
        # Create recipe to be updated
        recipe = Recipe.objects.create(
            #id:1  # hard coded id
            name="Pizza",
            description="Put it in the oven"
        )
        Ingredient.objects.create(name="dough", recipe=recipe)
        Ingredient.objects.create(name="cheese", recipe=recipe)
        Ingredient.objects.create(name="tomato", recipe=recipe)

        # New ingredient list
        new_ingredients = [
            {"name": "casa tarradellas"}
        ]

        # UPDATE!
        response = self.client.patch(
            #f"/recipes/{1}/", # hard coded id
            f"/recipes/{recipe.pk}/",
            data={"ingredients": new_ingredients},
            content_type="application/json"
        )

        recipe.refresh_from_db()  # recipe is local var hence no need for self -.-!

        # Checking
        self.assertEqual(response.status_code, 200) # successful request
        self.assertEqual(recipe.ingredients.count(), 1)
        self.assertEqual(recipe.ingredients.first().name, "casa tarradellas")

    def test_delete_recipe(self):
        # Create recipe to be updated
        recipe = Recipe.objects.create(
            name="Pizza",
            description="Put it in the oven"
        )
        Ingredient.objects.create(name="dough", recipe=recipe)
        Ingredient.objects.create(name="cheese", recipe=recipe)
        Ingredient.objects.create(name="tomato", recipe=recipe)

        # Delete
        response = self.client.delete(
            f"/recipes/{recipe.pk}/"
        )

        # Checking
        self.assertEqual(response.status_code, 204)
        # Would be better to import status and do
        # self.assertEqual (response.status_code, status.HTTP_204_NO_CONTENT) ?

