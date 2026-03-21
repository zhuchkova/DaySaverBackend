INSERT INTO foods (
    name, source_name, description, category_id, data_source, fdc_id,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g, emoji
)
SELECT
    'Tea',
    'Tea',
    'Generic tea for image recognition',
    category_id,
    'Derived for DL',
    NULL,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g,
    '🫖'
FROM foods
WHERE name = 'Tea - black'
ON CONFLICT (name) DO NOTHING;

INSERT INTO foods (
    name, source_name, description, category_id, data_source, fdc_id,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g, emoji
)
SELECT
    'Coffee',
    'Coffee',
    'Generic coffee for image recognition',
    category_id,
    'Derived for DL',
    NULL,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g,
    '☕'
FROM foods
WHERE name = 'Coffee - brewed'
ON CONFLICT (name) DO NOTHING;

INSERT INTO foods (
    name, source_name, description, category_id, data_source, fdc_id,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g, emoji
)
SELECT
    'Juice',
    'Juice',
    'Generic juice for image recognition',
    category_id,
    'Derived for DL',
    NULL,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g,
    '🧃'
FROM foods
WHERE name = 'Juice - orange'
ON CONFLICT (name) DO NOTHING;

INSERT INTO foods (
    name, source_name, description, category_id, data_source, fdc_id,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g, emoji
)
SELECT
    'Bread',
    'Bread',
    'Generic bread for image recognition',
    category_id,
    'Derived for DL',
    NULL,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g,
    '🍞'
FROM foods
WHERE name = 'Bread - white'
ON CONFLICT (name) DO NOTHING;

INSERT INTO foods (
    name, source_name, description, category_id, data_source, fdc_id,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g, emoji
)
SELECT
    'Toast',
    'Toast',
    'Generic toast for image recognition',
    category_id,
    'Derived for DL',
    NULL,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g,
    '🍞'
FROM foods
WHERE name = 'Bread - white'
ON CONFLICT (name) DO NOTHING;

INSERT INTO foods (
    name, source_name, description, category_id, data_source, fdc_id,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g, emoji
)
SELECT
    'Yogurt',
    'Yogurt',
    'Generic yogurt for image recognition',
    category_id,
    'Derived for DL',
    NULL,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g,
    '🥣'
FROM foods
WHERE name = 'Yogurt - greek'
ON CONFLICT (name) DO NOTHING;

INSERT INTO foods (
    name, source_name, description, category_id, data_source, fdc_id,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g, emoji
)
SELECT
    'Milk', 'Milk', 'Generic milk for image recognition',
    category_id, 'Derived for DL', NULL,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g,
    '🥛'
FROM foods
WHERE name = 'Milk - whole'
ON CONFLICT (name) DO NOTHING;

INSERT INTO foods (
    name, source_name, description, category_id, data_source, fdc_id,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g, emoji
)
SELECT
    'Oatmeal', 'Oatmeal', 'Generic oatmeal for image recognition',
    category_id, 'Derived for DL', NULL,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g,
    '🥣'
FROM foods
WHERE name = 'Oatmeal - multigrain'
ON CONFLICT (name) DO NOTHING;

INSERT INTO foods (
    name, source_name, description, category_id, data_source, fdc_id,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g, emoji
)
SELECT
    'Syrup', 'Syrup', 'Generic syrup for image recognition',
    category_id, 'Derived for DL', NULL,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g,
    '🍯'
FROM foods
WHERE name = 'Syrup - maple'
ON CONFLICT (name) DO NOTHING;

INSERT INTO foods (
    name, source_name, description, category_id, data_source, fdc_id,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g, emoji
)
SELECT
    'Cheese', 'Cheese', 'Generic cheese for image recognition',
    category_id, 'Derived for DL', NULL,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g,
    '🧀'
FROM foods
WHERE name = 'Cheese - hard'
ON CONFLICT (name) DO NOTHING;

INSERT INTO foods (
    name, source_name, description, category_id, data_source, fdc_id,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g, emoji
)
SELECT
    'Salmon', 'Salmon', 'Generic salmon for image recognition',
    category_id, 'Derived for DL', NULL,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g,
    '🐟'
FROM foods
WHERE name = 'Smoked salmon'
ON CONFLICT (name) DO NOTHING;

INSERT INTO foods (
    name, source_name, description, category_id, data_source, fdc_id,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g, emoji
)
SELECT
    'Oil', 'Oil', 'Generic oil for image recognition',
    category_id, 'Derived for DL', NULL,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g,
    '🛢️'
FROM foods
WHERE name = 'Oil - olive'
ON CONFLICT (name) DO NOTHING;

INSERT INTO foods (
    name, source_name, description, category_id, data_source, fdc_id,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g, emoji
)
SELECT
    'Cocoa', 'Cocoa', 'Generic cocoa for image recognition',
    category_id, 'Derived for DL', NULL,
    kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g,
    fiber_g_per_100g, sugars_g_per_100g,
    '🍫'
FROM foods
WHERE name = 'Cocoa - powder'
ON CONFLICT (name) DO NOTHING;



