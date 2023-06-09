"""
URL mappings for the recipe API.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet #RecipeViewSet, IngredientViewSet,


# Create a router and register the RecipeAPIView as a viewset
router = DefaultRouter()
router.register('recipes', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

""" urlpatterns = [
    #path('recipes/create/', RecipeCreateAPIView.as_view()),
    path('recipes/', RecipeAPIView.as_view()),
] """


""" router = DefaultRouter()
router.register('recipeview', RecipeViewSet)
router.register('ingredients', IngredientViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
] """

