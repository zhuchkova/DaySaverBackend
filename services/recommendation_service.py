from schemas.analyze import (
    AnalyzeRequest,
    AnalyzeResponse,
    Macros,
    ResultBlock,
    RecommendationBlock,
    FoodBreakdown,
    SatietyBlock,
    SwapRecommendation,
    EnergyBlock,
    HungerBlock,
    IngredientCard,
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


def calculate_satiety_score(protein: float, fiber: float, fat: float) -> float:
    return protein + fiber * 2 + fat * 0.5


def categorize_satiety(score: float) -> str:
    if score < 12:
        return "Low"
    elif score < 25:
        return "Moderate"
    return "High"


def generate_result_messages(gl_category: str, protein: float, fiber: float, satiety_level: str) -> list[str]:
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

    if satiety_level == "Low":
        messages.append("It may not keep you full for very long.")
    elif satiety_level == "High":
        messages.append("It is likely to be quite filling.")

    return messages


def generate_recommendations(
    gl_category: str,
    protein: float,
    fiber: float,
    diet_type: str,
    satiety_level: str,
) -> list[str]:
    suggestions = []

    protein_sources = {
        "vegan": [
            "tofu",
            "hummus",
            "soy yogurt",
            "seeds",
        ],
        "vegetarian": [
            "Greek yogurt",
            "skyr",
            "eggs",
            "tofu",
        ],
        "omnivore": [
            "eggs",
            "Greek yogurt",
            "cottage cheese",
            "turkey slices",
        ],
    }

    chosen_protein_sources = protein_sources.get(diet_type, protein_sources["omnivore"])

    if gl_category == "High":
        suggestions.append(
            "Try pairing fast-digesting carbs with protein, fiber, or healthy fats to reduce spike risk."
        )

    if protein < 15:
        suggestions.append(
            f"Consider adding {chosen_protein_sources[0]}, {chosen_protein_sources[1]}, or {chosen_protein_sources[2]} for more protein."
        )

    if fiber < 6:
        suggestions.append("Add berries, vegetables, seeds, or whole-grain options to increase fiber.")

    if satiety_level == "Low" and len(suggestions) < 3:
        suggestions.append("Adding more protein, fiber, or healthy fats may help keep you full for longer.")

    if (gl_category == "High" or fiber < 6) and len(suggestions) < 3:
        suggestions.append("Adding avocado, nuts, or nut butter may help slow glucose absorption.")

    return suggestions[:3]


def generate_swap_recommendations(food_names: list[str]) -> list[SwapRecommendation]:
    swap_rules = {
        "Bread - white": ("Bread - whole grain", "lower glycemic load"),
        "Croissant": ("Eggs", "more protein and lower spike risk"),
        "Nutella": ("Butter - peanut", "more protein and less sugar"),
        "Jam": ("Butter - peanut", "less sugar and more satiety"),
        "Juice - orange": ("Oranges", "more fiber and lower glycemic load"),
        "Juice - apple": ("Apples", "more fiber and lower glycemic load"),
        "Milk - chocolate": ("Milk - whole", "less sugar"),
        "Yogurt - greek sweetened": ("Yogurt - greek", "less sugar"),
        "Sugar": ("Stevia", "lower glycemic impact"),
        "Waffle": ("Pancakes", "potentially easier to balance with protein"),
    }

    swaps = []
    seen = set()

    for food_name in food_names:
        if food_name in swap_rules and food_name not in seen:
            to_food, reason = swap_rules[food_name]
            swaps.append(
                SwapRecommendation(
                    from_food=food_name,
                    to_food=to_food,
                    reason=reason,
                )
            )
            seen.add(food_name)

    return swaps[:3]


def generate_energy_block(gl_category: str) -> tuple[str, str]:
    if gl_category == "High":
        return (
            "Good start, possible dip later",
            "Quick energy at first due to rapidly available carbohydrates."
        )
    elif gl_category == "Moderate":
        return (
            "Moderate energy pattern",
            "Energy may feel stable at first, with some chance of a dip later."
        )
    return (
        "More stable energy",
        "This meal is less likely to cause a rapid rise and fall in energy."
    )


def generate_hunger_block(gl_category: str, satiety_level: str) -> tuple[str, str]:
    if gl_category == "High" and satiety_level == "Low":
        return (
            "Blood Sugar & Hunger",
            "A fast rise followed by a drop may lead to earlier hunger and cravings."
        )
    elif gl_category == "High":
        return (
            "Blood Sugar & Hunger",
            "If blood sugar drops, the body may signal a need for quick energy, which can feel like hunger or sweet cravings before noon."
        )
    elif satiety_level == "Low":
        return (
            "Blood Sugar & Hunger",
            "Because this meal may not keep you full for long, hunger could come back sooner."
        )
    return (
        "Blood Sugar & Hunger",
        "This breakfast is more likely to support steadier fullness through the morning."
    )


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
    selected_food_names = []
    ingredient_cards = []
    seen_food_ids = set()

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

        selected_food_names.append(row["food_name"])

        if item.food_id not in seen_food_ids:
            ingredient_cards.append(
                IngredientCard(
                    food_id=item.food_id,
                    name=row["food_name"],
                    emoji=row.get("emoji"),
                    short_label=row.get("short_label") or "Breakfast Food",
                )
            )
            seen_food_ids.add(item.food_id)

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
    spike_category = categorize_gl(total_gl)

    satiety_score = calculate_satiety_score(total_protein, total_fiber, total_fat)
    satiety_level = categorize_satiety(satiety_score)

    energy_level, energy_message = generate_energy_block(spike_category)
    hunger_title, hunger_message = generate_hunger_block(spike_category, satiety_level)

    diet_type = "omnivore"
    if request.user_preferences and request.user_preferences.diet_type:
        diet_type = request.user_preferences.diet_type

    result_messages = generate_result_messages(
        spike_category,
        total_protein,
        total_fiber,
        satiety_level,
    )

    recommendation_suggestions = generate_recommendations(
        spike_category,
        total_protein,
        total_fiber,
        diet_type,
        satiety_level,
    )

    swaps = generate_swap_recommendations(selected_food_names)

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
        spike_category=spike_category,
        satiety=SatietyBlock(
            score=round(satiety_score, 1),
            level=satiety_level,
        ),
        energy=EnergyBlock(
            level=energy_level,
            message=energy_message,
        ),
        hunger=HungerBlock(
            title=hunger_title,
            message=hunger_message,
        ),
        ingredient_cards=ingredient_cards,
        result=ResultBlock(messages=result_messages),
        recommendation=RecommendationBlock(suggestions=recommendation_suggestions),
        swaps=swaps,
        foods=food_breakdown,
    )