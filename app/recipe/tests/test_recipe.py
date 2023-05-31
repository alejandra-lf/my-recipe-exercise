from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from recipe.models import Recipe, Ingredient

RECIPES_URL = reverse('recipe-list')


class RecipeViewSetTest(TestCase):
    # def setUp(self):
    #     self.client = APIClient()
    # if uncomment above lines then
    # response = self.client.post(RECIPES_URL, payload, content_type="application/json")  doesn't work, why???
    # some serialization stuff involved?

    def test_list_recipes(self):
        response = self.client.get(RECIPES_URL)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == Recipe.objects.count()
        # what else to assert?

    def test_create_recipe(self):
        payload = {
            "name": "Canned soup",
            "description": "Microwave it for 4 min",
            "ingredients": [
                {
                    "name": "cream"
                },
                {
                    "name": "mushrooms"
                }
            ]
        }

        response = self.client.post(
            RECIPES_URL, payload, content_type="application/json")
        # response = self.client.post(RECIPES_URL, payload, format="json")
        # content_type="application/json" VS format="json" ...difference?
        # print("Actual status code:", response.status_code)

        assert response.status_code == status.HTTP_201_CREATED

        #assert response.data['name'] == payload['name']
        #assert response.data['description'] == payload['description']
        #assert len(response.data['ingredients']) == 2

    def test_put_recipe(self):
        recipe = Recipe.objects.create(
            name="Pizza",
            description="Place it in the oven"
        )
        Ingredient.objects.create(name="dough", recipe=recipe)
        Ingredient.objects.create(name="tomato", recipe=recipe)

        detail_url = reverse('recipe-detail', args=[recipe.id])

        payload = {
            "name": "Pizza",
            "description": "Place it in the oven",
            "ingredients": [
                {
                    "name": "dough"
                },
                {
                    "name": "cheese"
                }
            ]
        }

        response = self.client.put(
            detail_url, payload, content_type="application/json")

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == payload['name']
        assert response.data['description'] == payload['description']
        assert len(response.data['ingredients']) == 2

    def test_patch_recipe(self):
        recipe = Recipe.objects.create(
            name="Tomato Pizza",
            description="Place it in the oven"
        )
        Ingredient.objects.create(name="dough", recipe=recipe)
        Ingredient.objects.create(name="tomato", recipe=recipe)

        detail_url = reverse('recipe-detail', args=[recipe.id])
        payload = {
            "name": "New Pizza",
            "ingredients": []
        }

        response = self.client.patch(
            detail_url, payload, content_type="application/json")

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == payload['name']
        assert response.data['description'] == "Place it in the oven"
        assert len(response.data['ingredients']) == 0

    def test_destroy_recipe(self):
        # Create a recipe to destroy
        payload = {
            # "id" : 3,
            "name": "Canned soup",
            "description": "Microwave it for 4 min",
            "ingredients": [
                {
                    "name": "cream"
                },
                {
                    "name": "mushrooms"
                }
            ]
        }

        response = self.client.post(
            RECIPES_URL, payload, content_type="application/json")
        assert response.status_code == status.HTTP_201_CREATED

        # Destroy it
        print("Response content:", response.data)
        # -------- now response.data is jus a string "Recipe successfully created", so test failing
        # it fails also when hardcoding de id in payload {"id": 1}    :'(
        recipe_id = response.data['id']  # payload['id']
        detail_url = reverse('recipe-detail', args=[recipe_id])
        response = self.client.delete(detail_url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        # what else to test?

        # detail_url = reverse('recipe-detail', args=[recipe_id]) repeats on almost every test... -.-!
        # is something like "RECIPES_URL = reverse('recipe-list')" possible?




        # print("Response content:", response.content)
        # print("Response content:", response.data)