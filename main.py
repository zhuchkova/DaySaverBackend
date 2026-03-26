# uvicorn main:app --reload
from fastapi import FastAPI, Query, HTTPException, Body, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from psycopg.rows import dict_row
import psycopg
from dotenv import load_dotenv
import os
from pathlib import Path

from schemas.analyze import AnalyzeRequest, AnalyzeResponse
from services.recommendation_service import analyze_meal


from schemas.image_detection import DetectFromImageResponse
from services.image_detection_service import (
    build_candidate_catalog,
    detect_from_image_with_gemini,
)
import tempfile

load_dotenv()

app = FastAPI(title="DaySaver API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
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
                    "value": float(row["gi_index"]) if row["gi_index"] is not None else None,
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
def analyze(
    request: AnalyzeRequest = Body(
        ...,
        openapi_examples={
            "croissant_and_juice": {
                "summary": "Croissant and orange juice (omnivore)",
                "description": "Example breakfast with croissant and orange juice",
                "value": {
                    "items": [
                        {
                            "food_id": 148,
                            "portion_id": 196,
                            "quantity": 1
                        },
                        {
                            "food_id": 18,
                            "portion_id": 53,
                            "quantity": 1
                        }
                    ],
                    "user_preferences": {
                        "diet_type": "omnivore"
                    }
                },
            },
            "bread_and_avocado": {
                "summary": "White bread and avocado (vegetarian)",
                "description": "Example breakfast with white bread and avocado",
                "value": {
                    "items": [
                        {
                            "food_id": 8,
                            "portion_id": 23,
                            "quantity": 1
                        },
                        {
                            "food_id": 156,
                            "portion_id": 221,
                            "quantity": 1
                        }
                    ],
                    "user_preferences": {
                        "diet_type": "vegetarian"
                    }
                },
            },
        },
    )
):
    food_ids = [item.food_id for item in request.items]
    portion_ids = [item.portion_id for item in request.items]

    if not food_ids:
        raise HTTPException(status_code=400, detail="No foods provided")

    query = """
            SELECT f.id     AS food_id,
                   f.name   AS food_name,
                   f.emoji,
                   fi.short_label,
                   f.kcal_per_100g,
                   f.protein_g_per_100g,
                   f.fat_g_per_100g,
                   f.carbs_g_per_100g,
                   f.fiber_g_per_100g,
                   f.sugars_g_per_100g,
                   gi.value AS gi_index,
                   p.id     AS portion_id,
                   p.label  AS portion_label,
                   p.gram_weight
            FROM foods f
                     JOIN portions p ON p.food_id = f.id
                     LEFT JOIN gi ON gi.food_id = f.id
                     LEFT JOIN food_insights fi ON fi.food_id = f.id
            WHERE f.id = ANY (%(food_ids)s)
              AND p.id = ANY (%(portion_ids)s)
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


@app.get("/api/v1/foods/{food_id}/insight")
def get_food_insight(food_id: int):
    query = """
    SELECT
        f.id AS food_id,
        f.name,
        f.emoji,
        fi.short_label,
        fi.theme,
        fi.headline,
        fi.subtitle,
        fi.body,
        fi.effects,
        fi.warning_title,
        fi.warning_body,
        fi.education_title,
        fi.education_body,
        fi.highlight_title,
        fi.highlight_points
    FROM foods f
    JOIN food_insights fi ON fi.food_id = f.id
    WHERE f.id = %(food_id)s
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, {"food_id": food_id})
            row = cur.fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="Food insight not found")

    return row


def get_detection_candidates():
    query = """
    SELECT
        f.id AS food_id,
        f.name AS food_name,
        f.emoji,
        f.description,
        p.id AS portion_id,
        p.label AS portion_label
    FROM foods f
    JOIN portions p ON p.food_id = f.id
    WHERE f.use_for_detection = TRUE
    ORDER BY f.name, p.display_order;
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()


@app.post(
    "/api/v1/detect-from-image",
    response_model=DetectFromImageResponse,
    summary="Detect breakfast items from an image",
    description="""
        Upload a breakfast photo as **multipart/form-data**.
    
        ### 📸 What to upload:
        - A clear image of a breakfast meal
        - Prefer a top-down or slightly angled photo
        - Use good lighting
        - Make sure ingredients are visible and not heavily covered
    
        ### 🧠 What happens:
        - Gemini detects foods from the image
        - The backend maps them to existing `food_id` and `portion_id` values from the app database
        - The response returns editable detected items that can be reviewed before analysis
    
        ### ✅ Detectable foods for now:
        The current demo is optimized for common breakfast foods, especially:
        - eggs, fried eggs, omelet, bacon, salami, smoked salmon
        - bread, toast, croissant, pancakes, waffles, oatmeal, muesli, granola
        - yogurt, skyr, milk
        - coffee, tea, juice, cocoa
        - cucumber, tomato, avocado, bell peppers
        - common toppings such as syrup, jam, honey, peanut butter
        - selected fruits such as berries, banana, apple, orange, kiwi
    
        ### ✏️ How to use the result:
        - Show detected items to the user
        - Allow editing (remove / adjust / add manually)
        - Send the final confirmed selection to `/api/v1/analyze`
    
        ### ⚠️ Notes:
        - AI output is an estimate and may miss some foods
        - Unknown foods are ignored instead of guessed
        - Generic items such as `Tea`, `Coffee`, `Juice`, `Bread`, or `Toast` may be used when the image is not specific enough
        """,
    responses={
        400: {"description": "Invalid image upload"},
        500: {"description": "AI detection failed"},
    },
                )
async def detect_from_image(
    file: UploadFile = File(..., description="Breakfast image (jpg, jpeg, png)")
):
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        raise HTTPException(status_code=500, detail="GOOGLE_API_KEY is not configured")

    # ✅ Save uploaded file temporarily
    filename = file.filename or ""
    suffix = Path(filename).suffix if "." in filename else ".jpg"

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            contents = await file.read()
            tmp.write(contents)
            temp_path = tmp.name
    except Exception:
        raise HTTPException(status_code=400, detail="Failed to process uploaded file")

    #Get candidate foods
    try:
        candidate_rows = get_detection_candidates()
        candidate_catalog = build_candidate_catalog(candidate_rows)
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to load candidate foods")

    #Call Gemini
    try:
        gemini_result = detect_from_image_with_gemini(
            image_path=temp_path,
            api_key=google_api_key,
            candidate_catalog=candidate_catalog,
            model_name="gemini-2.5-flash",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image detection failed: {str(e)}")

    #Validate + map results
    row_map = {
        (row["food_id"], row["portion_id"]): row
        for row in candidate_rows
    }

    items = []
    for detected in gemini_result.detected_items:
        key = (detected.food_id, detected.portion_id)
        row = row_map.get(key)

        if not row:
            continue  # skip hallucinated items

        items.append({
            "food_id": row["food_id"],
            "food_name": row["food_name"],
            "emoji": row.get("emoji"),
            "portion_id": row["portion_id"],
            "portion_label": row["portion_label"],
            "quantity": detected.quantity,
            "reason": detected.reason,
        })

    #Final response
    return {
        "image_summary": {
            "detected_count": len(items),
            "confidence_percent": 90 if items else 0
        },
        "items": items
    }