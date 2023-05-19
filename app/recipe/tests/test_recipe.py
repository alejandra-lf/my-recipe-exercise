# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from recipe.serializers import RecipeSerializer

class CreateRecipeTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

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
        # would be nice to check aldo the ingredients name... umm for lopp maybe?
        # what else to check?
        # shouldn't I check smthg related with the models ?.. feel quite lost here