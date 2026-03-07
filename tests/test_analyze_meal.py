import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from schemas.analyze import AnalyzeRequest, UserPreferences, MealItem
from services.recommendation_service import analyze_meal


def test_analyze_meal_single_item():
    mock_rows = [
        {
            "food_id": 1,
            "food_name": "White bread",
            "portion_id": 1,
            "portion_label": "1 slice",
            "gram_weight": 50,
            "kcal_per_100g": 265,
            "protein_g_per_100g": 9,
            "fat_g_per_100g": 3.2,
            "carbs_g_per_100g": 49,
            "fiber_g_per_100g": 2.7,
            "sugars_g_per_100g": 5,
            "gi_index": 75,
        }
    ]

    request = AnalyzeRequest(
        items=[MealItem(food_id=1, portion_id=1, quantity=1)],
        user_preferences=UserPreferences(diet_type="vegan"),
    )

    result = analyze_meal(request, mock_rows)

    assert result.total_grams == 50.0
    assert result.total_macros.kcal == 132.5
    assert round(result.total_macros.protein_g, 1) == 4.5
    assert round(result.total_macros.carbs_g, 1) == 24.5
    assert result.spike_category in ["Low", "Moderate", "High"]
    assert len(result.foods) == 1
    assert result.foods[0].food_name == "White bread"


def test_analyze_meal_two_foods():
    mock_rows = [
        {
            "food_id": 1,
            "food_name": "White bread",
            "portion_id": 1,
            "portion_label": "1 slice",
            "gram_weight": 50,
            "kcal_per_100g": 265,
            "protein_g_per_100g": 9,
            "fat_g_per_100g": 3.2,
            "carbs_g_per_100g": 49,
            "fiber_g_per_100g": 2.7,
            "sugars_g_per_100g": 5,
            "gi_index": 75,
        },
        {
            "food_id": 2,
            "food_name": "Avocado",
            "portion_id": 2,
            "portion_label": "1/2 avocado",
            "gram_weight": 75,
            "kcal_per_100g": 160,
            "protein_g_per_100g": 2,
            "fat_g_per_100g": 15,
            "carbs_g_per_100g": 9,
            "fiber_g_per_100g": 7,
            "sugars_g_per_100g": 0.7,
            "gi_index": 15,
        },
    ]

    request = AnalyzeRequest(
        items=[
            MealItem(food_id=1, portion_id=1, quantity=1),
            MealItem(food_id=2, portion_id=2, quantity=1),
        ],
        user_preferences=UserPreferences(diet_type="vegetarian"),
    )

    result = analyze_meal(request, mock_rows)

    assert result.total_grams == 125.0
    assert len(result.foods) == 2
    assert result.total_macros.kcal > 0
    assert result.total_macros.fiber_g > 0
    assert result.average_glycemic_index > 0
    assert result.total_glycemic_load > 0
    assert result.spike_category in ["Low", "Moderate", "High"]


def test_analyze_meal_ignores_missing_food_portion_pair():
    mock_rows = [
        {
            "food_id": 1,
            "food_name": "White bread",
            "portion_id": 1,
            "portion_label": "1 slice",
            "gram_weight": 50,
            "kcal_per_100g": 265,
            "protein_g_per_100g": 9,
            "fat_g_per_100g": 3.2,
            "carbs_g_per_100g": 49,
            "fiber_g_per_100g": 2.7,
            "sugars_g_per_100g": 5,
            "gi_index": 75,
        }
    ]

    request = AnalyzeRequest(
        items=[
            MealItem(food_id=999, portion_id=999, quantity=1),  # missing pair
        ],
        user_preferences=UserPreferences(diet_type="omnivore"),
    )

    result = analyze_meal(request, mock_rows)

    assert result.total_grams == 0.0
    assert result.total_macros.kcal == 0.0
    assert result.total_glycemic_load == 0.0
    assert result.average_glycemic_index == 50.0
    assert len(result.foods) == 0