WITH mapping(new_food_id, source_food_id) AS (
    VALUES
        (188, 175), -- Tea <- Tea - black
        (189, 168), -- Coffee <- Coffee - brewed
        (190, 18),  -- Juice <- Juice - orange
        (191, 8),   -- Bread <- Bread - white
        (192, 8),   -- Toast <- Bread - white
        (193, 146), -- Yogurt <- Yogurt - greek
        (194, 10),  -- Milk <- Milk - whole
        (195, 1),   -- Oatmeal <- Oatmeal - multigrain
        (196, 125), -- Syrup <- Syrup - maple
        (197, 132), -- Cheese <- Cheese - hard
        (198, 141), -- Salmon <- Smoked salmon
        (199, 154), -- Oil <- Oil - olive
        (200, 179)  -- Cocoa <- Cocoa - powder
)
INSERT INTO gi (food_id, value, gi_category_id, data_source)
SELECT
    m.new_food_id,
    g.value,
    g.gi_category_id,
    g.data_source
FROM mapping m
JOIN gi g ON g.food_id = m.source_food_id
ON CONFLICT (food_id) DO NOTHING;

WITH mapping(new_food_id, source_food_id) AS (
    VALUES
        (188, 175),
        (189, 168),
        (190, 18),
        (191, 8),
        (192, 8),
        (193, 146),
        (194, 10),
        (195, 1),
        (196, 125),
        (197, 132),
        (198, 141),
        (199, 154),
        (200, 179)
)
INSERT INTO portions (label, unit_name, gram_weight, food_id, display_order)
SELECT
    p.label,
    p.unit_name,
    p.gram_weight,
    m.new_food_id,
    p.display_order
FROM mapping m
JOIN portions p ON p.food_id = m.source_food_id
ON CONFLICT (food_id, display_order) DO NOTHING;

WITH mapping(new_food_id, source_food_id) AS (
    VALUES
        (188, 175),
        (189, 168),
        (190, 18),
        (191, 8),
        (192, 8),
        (193, 146),
        (194, 10),
        (195, 1),
        (196, 125),
        (197, 132),
        (198, 141),
        (199, 154),
        (200, 179)
)
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
SELECT
    m.new_food_id,
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
FROM mapping m
JOIN food_insights fi ON fi.food_id = m.source_food_id
ON CONFLICT (food_id) DO NOTHING;

UPDATE food_insights
SET
    short_label = 'Refined Carb',
    body = 'Toast is usually made from refined bread and can provide quick energy, but often with less fiber than whole-grain options.'
WHERE food_id = 192;

UPDATE food_insights
SET
    short_label = 'Quick Sugar',
    body = 'Juice contains sugar with little or no fiber compared with whole fruit, so it can raise blood sugar more quickly.'
WHERE food_id = 190;

