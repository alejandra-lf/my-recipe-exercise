"""
Views for recipe API
"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import RecipeSerializer
from .models import Recipe

class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    # Overriding list...
    # Search view by 'name' substring
    def list(self, request, *args, **kwargs):
        name = self.request.query_params.get('name', None)
        queryset = self.queryset
        if name:
            queryset = queryset.filter(name__icontains=name)
            print(queryset)
            serializer = RecipeSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            # Retrieve all recipes
            return super().list(request, *args, **kwargs)
