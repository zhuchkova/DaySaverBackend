from pydantic import BaseModel
from typing import List, Optional


class DetectedMealItem(BaseModel):
    food_id: int
    food_name: str
    emoji: Optional[str] = None
    portion_id: int
    portion_label: str
    quantity: int = 1
    reason: Optional[str] = None


class ImageSummary(BaseModel):
    detected_count: int
    confidence_percent: int


class DetectFromImageResponse(BaseModel):
    image_summary: ImageSummary
    items: List[DetectedMealItem]

    model_config = {
        "json_schema_extra": {
            "example": {
                "image_summary": {
                    "detected_count": 4,
                    "confidence_percent": 92
                },
                "items": [
                    {
                        "food_id": 192,
                        "food_name": "Toast",
                        "emoji": "🍞",
                        "portion_id": 402,
                        "portion_label": "2 slices",
                        "quantity": 1,
                        "reason": "Two slices of toast are visible on the plate."
                    },
                    {
                        "food_id": 158,
                        "food_name": "Cucumber",
                        "emoji": "🥒",
                        "portion_id": 307,
                        "portion_label": "5 slices",
                        "quantity": 1,
                        "reason": "Several cucumber slices are visible."
                    },
                    {
                        "food_id": 143,
                        "food_name": "Salami",
                        "emoji": "🥓",
                        "portion_id": 290,
                        "portion_label": "3 slices",
                        "quantity": 1,
                        "reason": "Sliced salami is visible."
                    },
                    {
                        "food_id": 189,
                        "food_name": "Coffee",
                        "emoji": "☕",
                        "portion_id": 350,
                        "portion_label": "medium cup",
                        "quantity": 1,
                        "reason": "A cup of coffee is visible."
                    }
                ]
            }
        }
    }