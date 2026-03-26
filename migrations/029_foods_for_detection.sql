UPDATE foods
SET use_for_detection = TRUE
WHERE id IN (
    8,    -- Bread - white
    21,   -- Tomato
    129,  -- Eggs
    131,  -- Eggs - omelet
    137,  -- Yogurt - skyr
    141,  -- Smoked salmon
    143,  -- Salami
    156,  -- Avocado
    158,  -- Cucumber
    179,  -- Cocoa - powder
    188,  -- Tea
    189,  -- Coffee
    190,  -- Juice
    191,  -- Bread
    192,  -- Toast
    193,  -- Yogurt
    194,  -- Milk
    195,  -- Oatmeal
    196,  -- Syrup
    197,  -- Cheese
    198,  -- Salmon
    199,  -- Oil
    200,  -- Cocoa
    201   -- Eggs - fried
);