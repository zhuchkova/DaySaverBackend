import json
import mimetypes
from pathlib import Path
from typing import Any

from google import genai
from pydantic import BaseModel


class GeminiDetectedItem(BaseModel):
    food_id: int
    portion_id: int
    quantity: int = 1
    reason: str | None = None


class GeminiDetectionResult(BaseModel):
    detected_items: list[GeminiDetectedItem]


def build_candidate_catalog(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Convert DB rows into compact candidate food objects for Gemini.
    Group by food_id and keep allowed portions under each food.
    """
    foods: dict[int, dict[str, Any]] = {}

    for row in rows:
        food_id = row["food_id"]
        if food_id not in foods:
            foods[food_id] = {
                "food_id": food_id,
                "food_name": row["food_name"],
                "description": row.get("description"),
                "emoji": row.get("emoji"),
                "allowed_portions": [],
            }

        if row.get("portion_id") is not None:
            foods[food_id]["allowed_portions"].append(
                {
                    "portion_id": row["portion_id"],
                    "portion_label": row["portion_label"],
                }
            )

    return list(foods.values())


def build_detection_prompt(candidate_catalog: list[dict[str, Any]]) -> str:
    return f"""
            You are identifying breakfast ingredients for an app.
            
            Rules:
            1. You must choose only from the provided candidate foods.
            2. For each chosen food, you must choose one allowed portion_id from that food's allowed_portions list.
            3. Do not invent foods, portions, IDs, or labels.
            4. If uncertain, leave the item out.
            5. Prefer simpler generic foods such as Tea, Coffee, Juice, Bread, Toast, Yogurt, Milk, Oatmeal, Syrup, Cheese, Salmon, Oil, Cocoa when the image is not specific enough.
            6. Return only JSON matching the required schema.
            
            Candidate foods:
            {json.dumps(candidate_catalog, ensure_ascii=False, indent=2)}
            """.strip()


def detect_from_image_with_gemini(
    image_path: str,
    api_key: str,
    candidate_catalog: list[dict[str, Any]],
    model_name: str = "gemini-2.5-flash",
) -> GeminiDetectionResult:
    """
    Send an image + constrained prompt to Gemini and parse structured output.
    """
    client = genai.Client(api_key=api_key)

    mime_type, _ = mimetypes.guess_type(image_path)
    if not mime_type:
        mime_type = "image/jpeg"

    prompt = build_detection_prompt(candidate_catalog)

    with open(image_path, "rb") as f:
        image_bytes = f.read()

    response = client.models.generate_content(
        model=model_name,
        contents=[
            prompt,
            {
                "inline_data": {
                    "mime_type": mime_type,
                    "data": image_bytes,
                }
            },
        ],
        config={
            "response_mime_type": "application/json",
            "response_schema": GeminiDetectionResult,
            "temperature": 0,
        },
    )

    # The official docs recommend structured outputs / JSON schema when one
    # strictly needs schema-shaped results. They also note Pydantic support in Python. :contentReference[oaicite:2]{index=2}
    if not response.parsed:
        raise ValueError("Gemini returned no parsed structured response")

    return response.parsed