UPDATE foods
SET use_for_detection = TRUE
WHERE id IN (
    -- existing core breakfast items
    1,   -- Oatmeal - multigrain
    2,   -- Muesli
    5,   -- Oatmeal - instant
    7,   -- Bread - whole grain
    8,   -- Bread - white
    10,  -- Milk - whole
    11,  -- Milk - skim
    12,  -- Yogurt - greek sweetened
    13,  -- Yogurt - greek low fat
    14,  -- Milk - chocolate
    15,  -- Milk - soy
    17,  -- Juice - apple
    18,  -- Juice - orange
    19,  -- Nuts - peanuts
    20,  -- Nuts - cashews

    -- fruits / visible toppings
    21,  -- Tomato
    22,  -- Carrots
    23,  -- Cherries
    107, -- Raspberries
    108, -- Apples
    110, -- Blueberries
    111, -- Strawberries
    114, -- Oranges
    117, -- Kiwi
    118, -- Bananas

    -- sweet breakfast items
    122, -- Nutella
    125, -- Syrup - maple
    127, -- Honey
    128, -- Waffle
    147, -- Pancakes
    148, -- Croissant
    149, -- Granola
    164, -- Jam

    -- eggs / dairy / protein
    129, -- Eggs
    130, -- Eggs - benedict
    131, -- Eggs - omelet
    132, -- Cheese - hard
    134, -- Cheese - cottage
    137, -- Yogurt - skyr
    138, -- Tofu
    139, -- Bacon
    141, -- Smoked salmon
    143, -- Salami
    144, -- Turkey slices
    146, -- Yogurt - greek
    151, -- Butter - peanut

    -- fats / seeds / vegetables
    152, -- Nuts - walnuts
    153, -- Nuts - almonds
    155, -- Chia seeds
    156, -- Avocado
    157, -- Guacamole
    158, -- Cucumber
    159, -- Bell pepper - green
    160, -- Bell pepper - orange
    161, -- Bell pepper - red
    162, -- Bell pepper - yellow

    -- drinks / powders
    166, -- Milk - oat
    167, -- Milk - almond
    168, -- Coffee - brewed
    169, -- Coffee - espresso
    170, -- Coffee - latte
    171, -- Coffee - cappuccino
    172, -- Coffee - turkish
    174, -- Tea - herbal
    175, -- Tea - black
    176, -- Tea - green
    177, -- Tea - with milk
    178, -- Hot chocolate - cocoa
    179, -- Cocoa - powder
    180, -- Cocoa - with milk

    -- simplified generic detection foods
    188, -- Tea
    189, -- Coffee
    190, -- Juice
    191, -- Bread
    192, -- Toast
    193, -- Yogurt
    194, -- Milk
    195, -- Oatmeal
    196, -- Syrup
    197, -- Cheese
    198, -- Salmon
    199, -- Oil
    200, -- Cocoa

    -- new
    201  -- Eggs - fried
);