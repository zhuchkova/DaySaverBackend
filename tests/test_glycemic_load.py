import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from services.recommendation_service import calculate_glycemic_load, categorize_gl


def test_calculate_glycemic_load_basic():
    gl = calculate_glycemic_load(carbs=30, fiber=5, gi=60)
    assert round(gl, 1) == 15.0


def test_calculate_glycemic_load_zero_available_carbs():
    gl = calculate_glycemic_load(carbs=5, fiber=10, gi=60)
    assert gl == 0.0


def test_categorize_gl_low():
    assert categorize_gl(5) == "Low"


def test_categorize_gl_moderate():
    assert categorize_gl(15) == "Moderate"


def test_categorize_gl_high():
    assert categorize_gl(25) == "High"