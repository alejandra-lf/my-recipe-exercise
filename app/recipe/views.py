"""
Views for recipe API

quite useful: https://testdriven.io/blog/drf-views-part-3/

"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import RecipeSerializer
from .models import Recipe
from .services import RecipeService


class RecipeViewSet(ViewSet):
    #queryset = Recipe.objects.all()

    def list(self, request):

        queryset = Recipe.objects.all()
        serializer = RecipeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


        """
        # Using DTO... not working
        # Exception Value: 1 validation error for RecipeDto ingredients value is not a valid list (type=type_error.list)
        recipes = RecipeService.get_all_recipes()
        serializer = RecipeSerializer(recipes, many=True)
        #return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # better to include the status. Examples in users/viewsets/userviewset/userviewset.py
        """

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
