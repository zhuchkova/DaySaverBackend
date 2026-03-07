from pydantic import BaseModel
from typing import List, Optional


class UserPreferences(BaseModel):
    diet_type: str = "omnivore"


class MealItem(BaseModel):
    food_id: int
    portion_id: int
    quantity: int = 1


class AnalyzeRequest(BaseModel):
    items: List[MealItem]
    user_preferences: Optional[UserPreferences] = None


class Macros(BaseModel):
    kcal: float
    protein_g: float
    fat_g: float
    carbs_g: float
    fiber_g: float
    sugars_g: float


class ResultBlock(BaseModel):
    messages: List[str]


class RecommendationBlock(BaseModel):
    suggestions: List[str]


class FoodBreakdown(BaseModel):
    food_id: int
    food_name: str
    portion_id: int
    portion_label: str
    total_grams: float
    glycemic_index: float
    glycemic_load: float
    macros: Macros


class AnalyzeResponse(BaseModel):
    total_grams: float
    total_macros: Macros
    average_glycemic_index: float
    total_glycemic_load: float
    spike_category: str
    result: ResultBlock
    recommendation: RecommendationBlock
    foods: List[FoodBreakdown]