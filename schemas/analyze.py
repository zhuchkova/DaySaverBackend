from pydantic import BaseModel, Field
from typing import List, Optional


class UserPreferences(BaseModel):
    diet_type: str = "omnivore"


class MealItem(BaseModel):
    food_id: int
    portion_id: int
    quantity: int = Field(default=1, ge=1)


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


class SwapRecommendation(BaseModel):
    from_food: str
    to_food: str
    reason: str


class SatietyBlock(BaseModel):
    score: float
    level: str


class EnergyBlock(BaseModel):
    level: str
    message: str


class HungerBlock(BaseModel):
    title: str
    message: str


class IngredientCard(BaseModel):
    food_id: int
    name: str
    emoji: Optional[str] = None
    short_label: str


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
    satiety: SatietyBlock
    energy: EnergyBlock
    hunger: HungerBlock
    ingredient_cards: List[IngredientCard]
    result: ResultBlock
    recommendation: RecommendationBlock
    swaps: List[SwapRecommendation]
    foods: List[FoodBreakdown]

    model_config = {
        "json_schema_extra": {
            "example": {
                "total_grams": 310,
                "total_macros": {
                    "kcal": 361.1,
                    "protein_g": 6.7,
                    "fat_g": 13.4,
                    "carbs_g": 53.2,
                    "fiber_g": 1.6,
                    "sugars_g": 27.5
                },
                "average_glycemic_index": 58.5,
                "total_glycemic_load": 30.2,
                "spike_category": "High",
                "satiety": {
                    "score": 16.6,
                    "level": "Moderate"
                },
                "energy": {
                    "level": "Good start, possible dip later",
                    "message": "Quick energy at first due to rapidly available carbohydrates."
                },
                "hunger": {
                    "title": "Blood Sugar & Hunger",
                    "message": "If blood sugar drops, the body may signal a need for quick energy, which can feel like hunger or sweet cravings before noon."
                },
                "ingredient_cards": [
                    {
                        "food_id": 148,
                        "name": "Croissant",
                        "emoji": "🥐",
                        "short_label": "Refined Carb"
                    },
                    {
                        "food_id": 18,
                        "name": "Juice - orange",
                        "emoji": "🧃",
                        "short_label": "Quick Sugar"
                    }
                ],
                "result": {
                    "messages": [
                        "This breakfast has a high estimated glucose spike risk.",
                        "The meal may digest quickly and lead to a faster rise in blood sugar.",
                        "Protein content is relatively low for a balanced breakfast.",
                        "Fiber is on the low side, which may reduce blood sugar stability."
                    ]
                },
                "recommendation": {
                    "suggestions": [
                        "Try pairing fast-digesting carbs with protein, fiber, or healthy fats to reduce spike risk.",
                        "Consider adding eggs, Greek yogurt, or cottage cheese for more protein.",
                        "Add berries, vegetables, seeds, or whole-grain options to increase fiber."
                    ]
                },
                "swaps": [
                    {
                        "from_food": "Croissant",
                        "to_food": "Eggs",
                        "reason": "more protein and lower spike risk"
                    },
                    {
                        "from_food": "Juice - orange",
                        "to_food": "Oranges",
                        "reason": "more fiber and lower glycemic load"
                    }
                ],
                "foods": [
                    {
                        "food_id": 148,
                        "food_name": "Croissant",
                        "portion_id": 196,
                        "portion_label": "1 croissant",
                        "total_grams": 60,
                        "glycemic_index": 67,
                        "glycemic_load": 17.4,
                        "macros": {
                            "kcal": 243.6,
                            "protein_g": 4.9,
                            "fat_g": 12.6,
                            "carbs_g": 27.5,
                            "fiber_g": 1.6,
                            "sugars_g": 6.8
                        }
                    },
                    {
                        "food_id": 18,
                        "food_name": "Juice - orange",
                        "portion_id": 53,
                        "portion_label": "medium glass",
                        "total_grams": 250,
                        "glycemic_index": 50,
                        "glycemic_load": 12.9,
                        "macros": {
                            "kcal": 117.5,
                            "protein_g": 1.8,
                            "fat_g": 0.8,
                            "carbs_g": 25.8,
                            "fiber_g": 0,
                            "sugars_g": 20.7
                        }
                    }
                ]
            }
        }
    }