import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from schemas.analyze import AnalyzeRequest, UserPreferences, MealItem
from services.recommendation_service import analyze_meal


def test_analyze_meal_single_item():
    mock_rows = [
        {
            "food_id": 8,
            "food_name": "Bread - white",
            "emoji": "🍞",
            "short_label": "Refined Carb",
            "portion_id": 23,
            "portion_label": "2 slices",
            "gram_weight": 60,
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
        items=[MealItem(food_id=8, portion_id=23, quantity=1)],
        user_preferences=UserPreferences(diet_type="vegan"),
    )

    result = analyze_meal(request, mock_rows)

    assert result.total_grams == 60.0
    assert round(result.total_macros.kcal, 1) == 159.0
    assert round(result.total_macros.protein_g, 1) == 5.4
    assert round(result.total_macros.carbs_g, 1) == 29.4
    assert result.spike_category in ["Low", "Moderate", "High"]

    assert result.satiety.score >= 0
    assert result.satiety.level in ["Low", "Moderate", "High"]

    assert result.energy.level
    assert result.energy.message
    assert result.hunger.title == "Blood Sugar & Hunger"
    assert result.hunger.message

    assert len(result.foods) == 1
    assert result.foods[0].food_name == "Bread - white"

    assert len(result.ingredient_cards) == 1
    assert result.ingredient_cards[0].food_id == 8
    assert result.ingredient_cards[0].name == "Bread - white"
    assert result.ingredient_cards[0].emoji == "🍞"
    assert result.ingredient_cards[0].short_label == "Refined Carb"

    assert len(result.result.messages) >= 1
    assert len(result.recommendation.suggestions) >= 1

    assert any(s.from_food == "Bread - white" for s in result.swaps)


def test_analyze_meal_two_foods_with_swap():
    mock_rows = [
        {
            "food_id": 8,
            "food_name": "Bread - white",
            "emoji": "🍞",
            "short_label": "Refined Carb",
            "portion_id": 23,
            "portion_label": "2 slices",
            "gram_weight": 60,
            "kcal_per_100g": 265,
            "protein_g_per_100g": 9,
            "fat_g_per_100g": 3.2,
            "carbs_g_per_100g": 49,
            "fiber_g_per_100g": 2.7,
            "sugars_g_per_100g": 5,
            "gi_index": 75,
        },
        {
            "food_id": 156,
            "food_name": "Avocado",
            "emoji": "🥑",
            "short_label": "Healthy Fats",
            "portion_id": 221,
            "portion_label": "1/2 avocado",
            "gram_weight": 100,
            "kcal_per_100g": 160,
            "protein_g_per_100g": 2,
            "fat_g_per_100g": 14.66,
            "carbs_g_per_100g": 8.53,
            "fiber_g_per_100g": 6.7,
            "sugars_g_per_100g": 0.66,
            "gi_index": 15,
        },
    ]

    request = AnalyzeRequest(
        items=[
            MealItem(food_id=8, portion_id=23, quantity=1),
            MealItem(food_id=156, portion_id=221, quantity=1),
        ],
        user_preferences=UserPreferences(diet_type="vegetarian"),
    )

    result = analyze_meal(request, mock_rows)

    assert result.total_grams == 160.0
    assert len(result.foods) == 2
    assert result.total_macros.kcal > 0
    assert result.total_macros.fiber_g > 0
    assert result.average_glycemic_index > 0
    assert result.total_glycemic_load > 0
    assert result.spike_category in ["Low", "Moderate", "High"]

    assert result.satiety.score >= 0
    assert result.satiety.level in ["Low", "Moderate", "High"]

    assert result.energy.level
    assert result.hunger.title == "Blood Sugar & Hunger"

    assert len(result.ingredient_cards) == 2
    assert any(card.food_id == 8 and card.short_label == "Refined Carb" for card in result.ingredient_cards)
    assert any(card.food_id == 156 and card.short_label == "Healthy Fats" for card in result.ingredient_cards)

    assert any(s.from_food == "Bread - white" for s in result.swaps)


def test_analyze_meal_ignores_missing_food_portion_pair():
    mock_rows = [
        {
            "food_id": 8,
            "food_name": "Bread - white",
            "emoji": "🍞",
            "short_label": "Refined Carb",
            "portion_id": 23,
            "portion_label": "2 slices",
            "gram_weight": 60,
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
        items=[MealItem(food_id=999, portion_id=999, quantity=1)],
        user_preferences=UserPreferences(diet_type="omnivore"),
    )

    result = analyze_meal(request, mock_rows)

    assert result.total_grams == 0.0
    assert result.total_macros.kcal == 0.0
    assert result.total_glycemic_load == 0.0
    assert result.average_glycemic_index == 50.0
    assert result.satiety.score == 0.0
    assert result.satiety.level == "Low"

    assert result.energy.level
    assert result.hunger.title == "Blood Sugar & Hunger"

    assert len(result.foods) == 0
    assert len(result.ingredient_cards) == 0
    assert len(result.swaps) == 0