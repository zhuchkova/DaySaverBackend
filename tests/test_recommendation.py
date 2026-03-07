from schemas.analyze import AnalyzeRequest, UserPreferences
from services.recommendation_service import analyze_food

mock_food = {
    "food_name": "White bread",
    "kcal_per_100g": 265,
    "protein_g_per_100g": 9,
    "fat_g_per_100g": 3.2,
    "carbs_g_per_100g": 49,
    "fiber_g_per_100g": 2.7,
    "sugars_g_per_100g": 5,
    "gi_index": 75,
}

request = AnalyzeRequest(
    food_id=1,
    portion_grams=50,
    quantity=1,
    user_preferences=UserPreferences(diet_type="vegan")
)

result = analyze_food(request, mock_food)

print(result.model_dump())