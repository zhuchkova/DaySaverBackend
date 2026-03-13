UPDATE categories
SET emoji = CASE name
    WHEN 'Cereals' THEN '🥣'
    WHEN 'Bread and Bakery' THEN '🍞'
    WHEN 'Dairy' THEN '🥛'
    WHEN 'Eggs' THEN '🍳'
    WHEN 'Fruits' THEN '🍓'
    WHEN 'Vegetables' THEN '🥬'
    WHEN 'Plant Proteins' THEN '⬜'
    WHEN 'Meat' THEN '🍖'
    WHEN 'Fish' THEN '🐟'
    WHEN 'Nuts and Seeds' THEN '🥜'
    WHEN 'Fats and Oils' THEN '🥑'
    WHEN 'Sweeteners' THEN '🍯'
    WHEN 'Beverages' THEN '☕'
    WHEN 'Snack Foods' THEN '🌯'
    WHEN 'Grains and Starches' THEN '🌾'
    ELSE '🍽️'
END;