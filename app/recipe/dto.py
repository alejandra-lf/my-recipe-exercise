from typing import List, Optional
from django.conf import settings
from pydantic import BaseModel


class IngredientDto(BaseModel):
    name: str




class RecipeDto(BaseModel):
    name: str
    description: str
    #ingredients: List[IngredientDto]
    ingredients: Optional[List[IngredientDto]]

    class Config:
        orm_mode = True

# dto example: RequestUserDto  from dto.py