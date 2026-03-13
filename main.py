from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from psycopg.rows import dict_row
import psycopg
from dotenv import load_dotenv
import os

from schemas.analyze import AnalyzeRequest, AnalyzeResponse
from services.recommendation_service import analyze_meal

load_dotenv()

app = FastAPI(title="DaySaver API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = os.getenv("DATABASE_URL")


def get_connection():
    return psycopg.connect(DATABASE_URL, row_factory=dict_row)


@app.get("/api/v1/catalog")
def get_catalog():
    query = """
        SELECT
            category_name,
            category_emoji,
            food_id,
            food_name,
            emoji,
            description,
            kcal_per_100g,
            protein_g_per_100g,
            fat_g_per_100g,
            carbs_g_per_100g,
            fiber_g_per_100g,
            sugars_g_per_100g,
            gi_index,
            gi_category,
            portion_id,
            portion_label,
            unit_name,
            gram_weight,
            display_order
        FROM foods_with_portions
        ORDER BY category_name, food_name, display_order;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()

    categories = {}

    for row in rows:
        category_name = row["category_name"]
        food_id = row["food_id"]

        if category_name not in categories:
            categories[category_name] = {
                "category_name": category_name,
                "category_emoji": row["category_emoji"],
                "foods": {}
            }

        if food_id not in categories[category_name]["foods"]:
            categories[category_name]["foods"][food_id] = {
                "food_id": food_id,
                "name": row["food_name"],
                "emoji": row["emoji"],
                "description": row["description"],
                "macros_per_100g": {
                    "kcal": float(row["kcal_per_100g"]) if row["kcal_per_100g"] is not None else None,
                    "protein_g": float(row["protein_g_per_100g"]) if row["protein_g_per_100g"] is not None else None,
                    "fat_g": float(row["fat_g_per_100g"]) if row["fat_g_per_100g"] is not None else None,
                    "carbs_g": float(row["carbs_g_per_100g"]) if row["carbs_g_per_100g"] is not None else None,
                    "fiber_g": float(row["fiber_g_per_100g"]) if row["fiber_g_per_100g"] is not None else None,
                    "sugars_g": float(row["sugars_g_per_100g"]) if row["sugars_g_per_100g"] is not None else None,
                },
                "gi": {
                    "value": float(row["gi_index"]) if row["gi_index"] is not None else None,
                    "category": row["gi_category"]
                },
                "portions": []
            }

        if row["portion_id"] is not None:
            categories[category_name]["foods"][food_id]["portions"].append({
                "portion_id": row["portion_id"],
                "label": row["portion_label"],
                "unit_name": row["unit_name"],
                "gram_weight": float(row["gram_weight"]),
                "display_order": row["display_order"]
            })

    result = []
    for category in categories.values():
        category["foods"] = list(category["foods"].values())
        result.append(category)

    return {"categories": result}


@app.get("/api/v1/foods/search")
def search_foods(q: str = Query(..., min_length=1)):
    query = """
        SELECT
            category_name,
            food_id,
            food_name,
            emoji,
            description,
            kcal_per_100g,
            protein_g_per_100g,
            fat_g_per_100g,
            carbs_g_per_100g,
            fiber_g_per_100g,
            sugars_g_per_100g,
            gi_index,
            gi_category,
            portion_id,
            portion_label,
            unit_name,
            gram_weight,
            display_order
        FROM foods_with_portions
        WHERE food_name ILIKE %(search)s
        ORDER BY food_name, display_order;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, {"search": f"%{q}%"})
            rows = cur.fetchall()

    foods = {}

    for row in rows:
        food_id = row["food_id"]

        if food_id not in foods:
            foods[food_id] = {
                "food_id": food_id,
                "name": row["food_name"],
                "emoji": row["emoji"],
                "description": row["description"],
                "category_name": row["category_name"],
                "macros_per_100g": {
                    "kcal": float(row["kcal_per_100g"]) if row["kcal_per_100g"] is not None else None,
                    "protein_g": float(row["protein_g_per_100g"]) if row["protein_g_per_100g"] is not None else None,
                    "fat_g": float(row["fat_g_per_100g"]) if row["fat_g_per_100g"] is not None else None,
                    "carbs_g": float(row["carbs_g_per_100g"]) if row["carbs_g_per_100g"] is not None else None,
                    "fiber_g": float(row["fiber_g_per_100g"]) if row["fiber_g_per_100g"] is not None else None,
                    "sugars_g": float(row["sugars_g_per_100g"]) if row["sugars_g_per_100g"] is not None else None,
                },
                "gi": {
                    "value": row["gi_index"],
                    "category": row["gi_category"]
                },
                "portions": []
            }

        if row["portion_id"] is not None:
            foods[food_id]["portions"].append({
                "portion_id": row["portion_id"],
                "label": row["portion_label"],
                "unit_name": row["unit_name"],
                "gram_weight": float(row["gram_weight"]),
                "display_order": row["display_order"]
            })

    return {
        "query": q,
        "foods": list(foods.values())
    }


@app.get("/api/v1/foods/{food_id}/portions")
def get_food_portions(food_id: int):
    query = """
    SELECT
        p.id,
        p.label,
        p.unit_name,
        p.gram_weight,
        p.display_order
    FROM portions p
    WHERE p.food_id = %(food_id)s
    ORDER BY p.display_order
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, {"food_id": food_id})
            rows = cur.fetchall()

    if not rows:
        raise HTTPException(status_code=404, detail="No portions found")

    portions = [
        {
            "portion_id": row["id"],
            "label": row["label"],
            "unit_name": row["unit_name"],
            "gram_weight": float(row["gram_weight"]),
            "display_order": row["display_order"],
        }
        for row in rows
    ]

    return {
        "food_id": food_id,
        "portions": portions
    }

@app.post("/api/v1/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest):
    if not request.items:
        raise HTTPException(status_code=400, detail="No foods provided")

    food_ids = [item.food_id for item in request.items]
    portion_ids = [item.portion_id for item in request.items]

    query = """
    SELECT
        f.id AS food_id,
        f.name AS food_name,
        f.kcal_per_100g,
        f.protein_g_per_100g,
        f.fat_g_per_100g,
        f.carbs_g_per_100g,
        f.fiber_g_per_100g,
        f.sugars_g_per_100g,
        gi.value AS gi_index,
        p.id AS portion_id,
        p.label AS portion_label,
        p.gram_weight
    FROM foods f
    JOIN portions p ON p.food_id = f.id
    LEFT JOIN gi ON gi.food_id = f.id
    WHERE f.id = ANY(%(food_ids)s)
      AND p.id = ANY(%(portion_ids)s)
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, {
                "food_ids": food_ids,
                "portion_ids": portion_ids
            })
            rows = cur.fetchall()

    if not rows:
        raise HTTPException(status_code=404, detail="No matching foods/portions found")

    return analyze_meal(request, rows)