import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.recommendation_service import (
    generate_result_messages,
    generate_recommendations,
    generate_swap_recommendations,
)


def test_generate_result_messages_high_gl_and_low_satiety():
    messages = generate_result_messages(
        gl_category="High",
        protein=10,
        fiber=3,
        satiety_level="Low",
    )

    assert any("high estimated glucose spike risk" in m.lower() for m in messages)
    assert any("protein content is relatively low" in m.lower() for m in messages)
    assert any("fiber is on the low side" in m.lower() for m in messages)
    assert any("may not keep you full" in m.lower() for m in messages)


def test_generate_result_messages_low_gl_and_high_satiety():
    messages = generate_result_messages(
        gl_category="Low",
        protein=28,
        fiber=11,
        satiety_level="High",
    )

    assert any("low estimated glucose spike risk" in m.lower() for m in messages)
    assert any("strong protein base" in m.lower() for m in messages)
    assert any("fiber content is strong" in m.lower() for m in messages)
    assert any("likely to be quite filling" in m.lower() for m in messages)


def test_generate_recommendations_vegan():
    suggestions = generate_recommendations(
        gl_category="High",
        protein=10,
        fiber=3,
        diet_type="vegan",
        satiety_level="Low",
    )

    assert any("tofu" in s.lower() or "hummus" in s.lower() or "soy yogurt" in s.lower() for s in suggestions)
    assert len(suggestions) <= 3


def test_generate_recommendations_vegetarian():
    suggestions = generate_recommendations(
        gl_category="Moderate",
        protein=10,
        fiber=3,
        diet_type="vegetarian",
        satiety_level="Moderate",
    )

    assert any("greek yogurt" in s.lower() or "skyr" in s.lower() or "eggs" in s.lower() for s in suggestions)
    assert len(suggestions) <= 3


def test_generate_recommendations_omnivore():
    suggestions = generate_recommendations(
        gl_category="Moderate",
        protein=10,
        fiber=3,
        diet_type="omnivore",
        satiety_level="Low",
    )

    assert any("eggs" in s.lower() or "cottage cheese" in s.lower() or "turkey slices" in s.lower() for s in suggestions)
    assert len(suggestions) <= 3


def test_generate_swap_recommendations():
    swaps = generate_swap_recommendations([
        "Bread - white",
        "Nutella",
        "Juice - orange",
    ])

    assert len(swaps) >= 1
    assert any(s.from_food == "Bread - white" and s.to_food == "Bread - whole grain" for s in swaps)
    assert any(s.from_food == "Nutella" and s.to_food == "Butter - peanut" for s in swaps)