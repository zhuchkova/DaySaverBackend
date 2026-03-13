DROP VIEW IF EXISTS foods_with_portions;

CREATE OR REPLACE VIEW foods_with_portions AS
SELECT
    c.name AS category_name,
    f.id AS food_id,
    f.name AS food_name,
    f.emoji,
    f.description,
    f.kcal_per_100g,
    f.protein_g_per_100g,
    f.fat_g_per_100g,
    f.carbs_g_per_100g,
    f.fiber_g_per_100g,
    f.sugars_g_per_100g,
    gi.value AS gi_index,
    gic.name AS gi_category,
    p.id AS portion_id,
    p.label AS portion_label,
    p.unit_name,
    p.gram_weight,
    p.display_order
FROM categories c
JOIN foods f ON f.category_id = c.id
LEFT JOIN gi ON gi.food_id = f.id
LEFT JOIN gi_categories gic ON gi.gi_category_id = gic.id
LEFT JOIN portions p ON p.food_id = f.id;