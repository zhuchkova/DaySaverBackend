import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from services.recommendation_service import scale_per_100g


def test_scale_per_100g_basic():
    assert scale_per_100g(200, 50) == 100.0
    assert scale_per_100g(10, 100) == 10.0
    assert scale_per_100g(0, 150) == 0.0


def test_scale_per_100g_none_value():
    assert scale_per_100g(None, 100) == 0.0


def test_scale_per_100g_decimal_like_values():
    assert round(scale_per_100g(265, 50), 1) == 132.5
    assert round(scale_per_100g(9, 50), 1) == 4.5