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
        pass

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
            return Response({"detail": "Recipe not found."}, status=status.HTTP_404_NOT_FOUND)


    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
