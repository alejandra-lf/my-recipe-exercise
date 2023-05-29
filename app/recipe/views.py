"""
Views for recipe API

quite useful: https://testdriven.io/blog/drf-views-part-3/

"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from .serializers import RecipeSerializer
from .models import Recipe
from .services import RecipeService


class RecipeViewSet(ViewSet):

    def list(self, request):
        # Using serializer (not DTO)
        # queryset = Recipe.objects.all()
        # serializer = RecipeSerializer(queryset, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

        # Using DTO... now working!!
        recipes = RecipeService.get_all_recipes()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # better to include the status. Examples in users/viewsets/userviewset/userviewset.py


    def create(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            # recipe = RecipeService.create_recipe(serializer.validated_data) # currently no need of having the recipe...
            RecipeService.create_recipe(serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED) #serializer.data,
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        # only serializer
        # recipe = get_object_or_404(Recipe.objects.filter(pk=pk))
        # serializer = RecipeSerializer(recipe)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            # e.g. aliasviewsets.py line 20
            # dto and services
            recipe = RecipeService.get_recipe(pk)
            serializer = RecipeSerializer(recipe)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Recipe not found."}, status=status.HTTP_404_NOT_FOUND)

    # put
    def update(self, request, pk=None):
        return RecipeViewSet._put_and_patch(pk, RecipeSerializer(data=request.data))
        # serializer = RecipeSerializer(data=request.data)
        # if serializer.is_valid():
        #     RecipeService.update_recipe(pk, serializer.validated_data)
        #     return Response("Recipe updated successfully.", status=status.HTTP_201_CREATED)
        # return Response("Failed to update recipe.", status=status.HTTP_400_BAD_REQUEST)

    # patch
    def partial_update(self, request, pk=None):
        return RecipeViewSet._put_and_patch(pk, RecipeSerializer(data=request.data, partial=True))
        # serializer = RecipeSerializer(data=request.data, partial=True)
        # if serializer.is_valid():
        #     RecipeService.update_recipe(pk, serializer.validated_data)
        #     return Response("Recipe updated successfully.", status=status.HTTP_201_CREATED)
        # return Response("Failed to update recipe.", status=status.HTTP_400_BAD_REQUEST)

    def _put_and_patch(pk,serializer):
        print(serializer)
        if serializer.is_valid():
            RecipeService.update_recipe(pk, serializer.validated_data)
            return Response("Recipe updated successfully.", status=status.HTTP_201_CREATED)
        return Response("Failed to update recipe.", status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            RecipeService.delete_recipe(pk)
            return Response("Recipe deleted successfully", status=status.HTTP_204_NO_CONTENT) # {"detail": "Recipe deleted."}
        except:
            # asuming that the pk doesn't exsit. Should be more specific handling the corresponding error
            return Response("Recipe not found.", status=status.HTTP_404_NOT_FOUND)



