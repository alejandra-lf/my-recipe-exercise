"""
Views for recipe API

quite useful: https://testdriven.io/blog/drf-views-part-3/

"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from .serializers import RecipeSerializer
from .services import RecipeService
from .models import Recipe



class RecipeViewSet(ViewSet):

    def list(self, request):
        try:
            recipes_dto = RecipeService.get_all_recipes()
            recipes_dict = [recipe_dto.dict() for recipe_dto in recipes_dto]
            return Response(data=recipes_dict, status=status.HTTP_200_OK)
        except:
            # serializer = RecipeSerializer(recipes, many=True)
            # return Response(serializer.data, status=status.HTTP_200_OK)
            return Response("No recipes to show", status=status.HTTP_404_NOT_FOUND)


    def retrieve(self, request, pk=None):
        try:
            # e.g. aliasviewsets.py line 20
            recipe_dto = RecipeService.get_recipe(pk)
            return Response(data=recipe_dto.dict(), status=status.HTTP_200_OK)
            # serializer = RecipeSerializer(recipe)
            # return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("Recipe not found.", status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            recipe_dto = RecipeService.create_recipe(serializer.validated_data)
            return Response(data=recipe_dto.dict(), status=status.HTTP_201_CREATED)
        return Response("Recipe not created.", status=status.HTTP_400_BAD_REQUEST)

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

    def _put_and_patch(pk, serializer):
        if serializer.is_valid():
            recipe_dto = RecipeService.update_recipe(
                pk, serializer.validated_data)
            return Response(data=recipe_dto.dict(), status=status.HTTP_201_CREATED)
        return Response("Failed to update recipe.", status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            RecipeService.delete_recipe(pk)
            return Response("Recipe successfully deleted", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response("Recipe not found.", status=status.HTTP_404_NOT_FOUND)
