from schemas.analyze import (
    AnalyzeRequest,
    AnalyzeResponse,
    Macros,
    ResultBlock,
    RecommendationBlock,
    FoodBreakdown,
)


def scale_per_100g(value_per_100g, grams: float) -> float:
    if value_per_100g is None:
        value_per_100g = 0
    return float(value_per_100g) * (float(grams) / 100)


def calculate_glycemic_load(carbs: float, fiber: float, gi: float) -> float:
    available_carbs = max(carbs - fiber, 0)
    return (gi * available_carbs) / 100


def categorize_gl(gl: float) -> str:
    if gl < 10:
        return "Low"
    elif gl < 20:
        return "Moderate"
    return "High"


def generate_result_messages(gl_category: str, protein: float, fiber: float) -> list[str]:
    messages = []

    if gl_category == "High":
        messages.append("This breakfast has a high estimated glucose spike risk.")
        messages.append("The meal may digest quickly and lead to a faster rise in blood sugar.")
    elif gl_category == "Moderate":
        messages.append("This breakfast has a moderate estimated glucose spike risk.")
    else:
        messages.append("This breakfast has a low estimated glucose spike risk.")

    if protein >= 25:
        messages.append("It provides a strong protein base, which can support satiety.")
    elif protein < 15:
        messages.append("Protein content is relatively low for a balanced breakfast.")

    if fiber < 6:
        messages.append("Fiber is on the low side, which may reduce blood sugar stability.")
    elif fiber >= 10:
        messages.append("Fiber content is strong and may help slow glucose absorption.")

    return messages


def generate_recommendations(
    gl_category: str,
    protein: float,
    fiber: float,
    diet_type: str,
) -> list[str]:
    suggestions = []

    if gl_category == "High":
        suggestions.append(
            "Try pairing fast-digesting carbs with protein, fiber, or healthy fats to reduce spike risk."
        )

    if protein < 15:
        if diet_type == "vegan":
            suggestions.append("Consider adding tofu, hummus, soy yogurt, or seeds for more protein.")
        elif diet_type == "vegetarian":
            suggestions.append("Consider adding Greek yogurt, skyr, eggs, or tofu for more protein.")
        else:
            suggestions.append("Consider adding eggs, Greek yogurt, cottage cheese, or lean meat for more protein.")

    if fiber < 6:
        suggestions.append("Add berries, vegetables, seeds, or whole-grain options to increase fiber.")

    if (gl_category == "High" or fiber < 6) and len(suggestions) < 3:
        suggestions.append("Adding avocado, nuts, or nut butter may help slow glucose absorption.")

    return suggestions[:3]


def analyze_meal(request: AnalyzeRequest, rows: list[dict]) -> AnalyzeResponse:
    row_map = {(row["food_id"], row["portion_id"]): row for row in rows}

    total_kcal = 0.0
    total_protein = 0.0
    total_fat = 0.0
    total_carbs = 0.0
    total_fiber = 0.0
    total_sugars = 0.0
    total_grams = 0.0
    total_gl = 0.0

    weighted_gi_sum = 0.0
    total_available_carbs = 0.0

    food_breakdown = []

    for item in request.items:
        row = row_map.get((item.food_id, item.portion_id))
        if not row:
            continue

        grams = float(row["gram_weight"]) * item.quantity

        kcal = scale_per_100g(row.get("kcal_per_100g"), grams)
        protein = scale_per_100g(row.get("protein_g_per_100g"), grams)
        fat = scale_per_100g(row.get("fat_g_per_100g"), grams)
        carbs = scale_per_100g(row.get("carbs_g_per_100g"), grams)
        fiber = scale_per_100g(row.get("fiber_g_per_100g"), grams)
        sugars = scale_per_100g(row.get("sugars_g_per_100g"), grams)

        gi = float(row["gi_index"]) if row.get("gi_index") is not None else 50.0
        gl = calculate_glycemic_load(carbs, fiber, gi)
        available_carbs = max(carbs - fiber, 0)

        total_kcal += kcal
        total_protein += protein
        total_fat += fat
        total_carbs += carbs
        total_fiber += fiber
        total_sugars += sugars
        total_grams += grams
        total_gl += gl

        weighted_gi_sum += gi * available_carbs
        total_available_carbs += available_carbs

        food_breakdown.append(
            FoodBreakdown(
                food_id=item.food_id,
                food_name=row["food_name"],
                portion_id=item.portion_id,
                portion_label=row["portion_label"],
                total_grams=round(grams, 1),
                glycemic_index=round(gi, 1),
                glycemic_load=round(gl, 1),
                macros=Macros(
                    kcal=round(kcal, 1),
                    protein_g=round(protein, 1),
                    fat_g=round(fat, 1),
                    carbs_g=round(carbs, 1),
                    fiber_g=round(fiber, 1),
                    sugars_g=round(sugars, 1),
                ),
            )
        )

    avg_gi = weighted_gi_sum / total_available_carbs if total_available_carbs > 0 else 50.0
    category = categorize_gl(total_gl)

    diet_type = "omnivore"
    if request.user_preferences and request.user_preferences.diet_type:
        diet_type = request.user_preferences.diet_type

    result_messages = generate_result_messages(category, total_protein, total_fiber)
    recommendation_suggestions = generate_recommendations(
        category,
        total_protein,
        total_fiber,
        diet_type,
    )

    return AnalyzeResponse(
        total_grams=round(total_grams, 1),
        total_macros=Macros(
            kcal=round(total_kcal, 1),
            protein_g=round(total_protein, 1),
            fat_g=round(total_fat, 1),
            carbs_g=round(total_carbs, 1),
            fiber_g=round(total_fiber, 1),
            sugars_g=round(total_sugars, 1),
        ),
        average_glycemic_index=round(avg_gi, 1),
        total_glycemic_load=round(total_gl, 1),
        spike_category=category,
        result=ResultBlock(messages=result_messages),
        recommendation=RecommendationBlock(suggestions=recommendation_suggestions),
        foods=food_breakdown,
    )