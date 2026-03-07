import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.recommendation_service import (
    generate_result_messages,
    generate_recommendations,
)


def test_generate_result_messages_high_gl():
    messages = generate_result_messages("High", protein=10, fiber=3)

    assert any("high estimated glucose spike risk" in m.lower() for m in messages)
    assert any("protein content is relatively low" in m.lower() for m in messages)
    assert any("fiber is on the low side" in m.lower() for m in messages)


def test_generate_result_messages_low_gl():
    messages = generate_result_messages("Low", protein=28, fiber=11)

    assert any("low estimated glucose spike risk" in m.lower() for m in messages)
    assert any("strong protein base" in m.lower() for m in messages)
    assert any("fiber content is strong" in m.lower() for m in messages)


def test_generate_recommendations_vegan():
    suggestions = generate_recommendations(
        "High",
        protein=10,
        fiber=3,
        diet_type="vegan",
    )

    assert any("tofu" in s.lower() or "hummus" in s.lower() or "soy yogurt" in s.lower() for s in suggestions)
    assert len(suggestions) <= 3


def test_generate_recommendations_vegetarian():
    suggestions = generate_recommendations(
        "Moderate",
        protein=10,
        fiber=3,
        diet_type="vegetarian",
    )

    assert any("greek yogurt" in s.lower() or "skyr" in s.lower() or "eggs" in s.lower() for s in suggestions)
    assert len(suggestions) <= 3


def test_generate_recommendations_omnivore():
    suggestions = generate_recommendations(
        "Moderate",
        protein=10,
        fiber=3,
        diet_type="omnivore",
    )

    assert any("eggs" in s.lower() or "lean meat" in s.lower() or "cottage cheese" in s.lower() for s in suggestions)
    assert len(suggestions) <= 3