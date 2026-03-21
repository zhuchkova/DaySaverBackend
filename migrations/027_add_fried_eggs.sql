INSERT INTO foods (
    id,
    name,
    source_name,
    description,
    category_id,
    data_source,
    fdc_id,
    kcal_per_100g,
    protein_g_per_100g,
    fat_g_per_100g,
    carbs_g_per_100g,
    fiber_g_per_100g,
    sugars_g_per_100g,
    emoji
)
VALUES (
    201,
    'Eggs - fried',
    'Eggs - fried',
    'Egg, whole, fried with oil',
    4,
    'Survey foods',
    '2707158',
    192,
    11.56,
    15.81,
    0.9,
    0,
    0.19,
    '🍳'
)
    ON CONFLICT (name) DO NOTHING;

INSERT INTO gi (
    food_id,
    value,
    gi_category_id,
    data_source
)
VALUES (
    201,
    0,
    1,
    NULL
)
    ON CONFLICT (food_id) DO NOTHING;

INSERT INTO portions (
    label,
    unit_name,
    gram_weight,
    food_id,
    display_order
)
VALUES
('1 fried egg', 'egg', 50, 201, 1),
('2 fried eggs', 'egg', 100, 201, 2),
('3 fried eggs', 'egg', 150, 201, 3)
    ON CONFLICT (food_id, display_order) DO NOTHING;

INSERT INTO food_insights (
    food_id,
    short_label,
    theme,
    headline,
    subtitle,
    body,
    effects,
    warning_title,
    warning_body,
    education_title,
    education_body,
    highlight_title,
    highlight_points
)
VALUES (
    201,
    'Protein + Fat',
    'protein',
    'How this ingredient affects your energy',
    'What happens in your body',
    'Fried eggs provide protein and fat, which can help support satiety and make breakfast more filling.',
    '["Can help you feel full longer", "May support steadier energy", "Contains both protein and fat"]'::jsonb,
    NULL,
    NULL,
    'Why protein helps',
    'Protein is digested more slowly than simple carbohydrates and can help reduce energy crashes later in the morning.',
    'Good breakfast role',
    '["Useful with bread", "Useful with vegetables", "Can help balance carb-based meals"]'::jsonb
);