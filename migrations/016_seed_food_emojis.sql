UPDATE foods
SET emoji = CASE id
    WHEN 1 THEN '🥣'   -- Oatmeal - multigrain
    WHEN 2 THEN '🥣'   -- Muesli
    WHEN 3 THEN '🥣'   -- Special K
    WHEN 4 THEN '🥣'   -- Cheerios
    WHEN 5 THEN '🥣'   -- Oatmeal - instant
    WHEN 6 THEN '🥣'   -- Cornflakes
    WHEN 7 THEN '🍞'   -- Bread - whole grain
    WHEN 8 THEN '🍞'   -- Bread - white
    WHEN 9 THEN '🥖'   -- Bread - baguette
    WHEN 10 THEN '🥛'  -- Milk - whole
    WHEN 11 THEN '🥛'  -- Milk - skim
    WHEN 12 THEN '🥣'  -- Yogurt - greek sweetened
    WHEN 13 THEN '🥣'  -- Yogurt - greek low fat
    WHEN 14 THEN '🥛'  -- Milk - chocolate
    WHEN 15 THEN '🥛'  -- Milk - soy
    WHEN 16 THEN '🧃'  -- Juice - tomato
    WHEN 17 THEN '🧃'  -- Juice - apple
    WHEN 18 THEN '🧃'  -- Juice - orange
    WHEN 19 THEN '🥜'  -- Nuts - peanuts
    WHEN 20 THEN '🥜'  -- Nuts - cashews
    WHEN 21 THEN '🍅'  -- Tomato
    WHEN 22 THEN '🥕'  -- Carrots
    WHEN 23 THEN '🍒'  -- Cherries

    WHEN 106 THEN '🍊' -- Grapefruit
    WHEN 107 THEN '🍇' -- Raspberries
    WHEN 108 THEN '🍎' -- Apples
    WHEN 109 THEN '🍐' -- Pears
    WHEN 110 THEN '🫐' -- Blueberries
    WHEN 111 THEN '🍓' -- Strawberries
    WHEN 112 THEN '🌴' -- Dates
    WHEN 113 THEN '🍑' -- Peaches
    WHEN 114 THEN '🍊' -- Oranges
    WHEN 115 THEN '🍇' -- Grapes - green
    WHEN 116 THEN '🍇' -- Grapes - red
    WHEN 117 THEN '🥝' -- Kiwi
    WHEN 118 THEN '🍌' -- Bananas
    WHEN 119 THEN '🍍' -- Pineapple
    WHEN 120 THEN '🍇' -- Raisins
    WHEN 121 THEN '🍉' -- Watermelon
    WHEN 122 THEN '🍫' -- Nutella
    WHEN 123 THEN '🧴' -- Stevia
    WHEN 124 THEN '🍯' -- Syrup - agave
    WHEN 125 THEN '🍁' -- Syrup - maple
    WHEN 126 THEN '🍮' -- Caramel
    WHEN 127 THEN '🍯' -- Honey
    WHEN 128 THEN '🧇' -- Waffle
    WHEN 129 THEN '🥚' -- Eggs
    WHEN 130 THEN '🍳' -- Eggs - benedict
    WHEN 131 THEN '🍳' -- Eggs - omelet
    WHEN 132 THEN '🧀' -- Cheese - hard
    WHEN 133 THEN '🧀' -- Cheese - protein
    WHEN 134 THEN '🧀' -- Cheese - cottage
    WHEN 135 THEN '🧀' -- Cheese - feta
    WHEN 136 THEN '🧀' -- Cheese - cream
    WHEN 137 THEN '🥣' -- Yogurt - skyr
    WHEN 138 THEN '⬜' -- Tofu
    WHEN 139 THEN '🥓' -- Bacon
    WHEN 140 THEN '🌭' -- Sausage
    WHEN 141 THEN '🐟' -- Smoked salmon
    WHEN 142 THEN '🍖' -- Ham slices
    WHEN 143 THEN '🍖' -- Salami
    WHEN 144 THEN '🍗' -- Turkey slices
    WHEN 145 THEN '🥥' -- Oil - coconut
    WHEN 146 THEN '🥣' -- Yogurt - greek
    WHEN 147 THEN '🥞' -- Pancakes
    WHEN 148 THEN '🥐' -- Croissant
    WHEN 149 THEN '🥣' -- Granola
    WHEN 150 THEN '🧈' -- Butter
    WHEN 151 THEN '🥜' -- Butter - peanut
    WHEN 152 THEN '🥜' -- Nuts - walnuts
    WHEN 153 THEN '🥜' -- Nuts - almonds
    WHEN 154 THEN '🫒' -- Oil - olive
    WHEN 155 THEN '🌱' -- Chia seeds
    WHEN 156 THEN '🥑' -- Avocado
    WHEN 157 THEN '🥑' -- Guacamole
    WHEN 158 THEN '🥒' -- Cucumber
    WHEN 159 THEN '🫑' -- Bell pepper - green
    WHEN 160 THEN '🫑' -- Bell pepper - orange
    WHEN 161 THEN '🫑' -- Bell pepper - red
    WHEN 162 THEN '🫑' -- Bell pepper - yellow
    WHEN 163 THEN '🍋' -- Lemon
    WHEN 164 THEN '🍓' -- Jam
    WHEN 165 THEN '🌯' -- Breakfast burrito
    WHEN 166 THEN '🥛' -- Milk - oat
    WHEN 167 THEN '🥛' -- Milk - almond
    WHEN 168 THEN '☕' -- Coffee - brewed
    WHEN 169 THEN '☕' -- Coffee - espresso
    WHEN 170 THEN '☕' -- Coffee - latte
    WHEN 171 THEN '☕' -- Coffee - cappuccino
    WHEN 172 THEN '☕' -- Coffee - turkish
    WHEN 173 THEN '🍚' -- Sugar
    WHEN 174 THEN '🫖' -- Tea - herbal
    WHEN 175 THEN '🫖' -- Tea - black
    WHEN 176 THEN '🫖' -- Tea - green
    WHEN 177 THEN '🫖' -- Tea - with milk
    WHEN 178 THEN '☕' -- Hot chocolate - cocoa
    WHEN 179 THEN '🍫' -- Cocoa - powder
    WHEN 180 THEN '☕' -- Cocoa - with milk
    WHEN 181 THEN '🥦' -- Broccoli
    WHEN 182 THEN '🍗' -- Chicken
    WHEN 183 THEN '🐟' -- Fish
    WHEN 184 THEN '🥬' -- Lettuce
    WHEN 185 THEN '🧅' -- Onions
    WHEN 186 THEN '🥔' -- Potatoes
    WHEN 187 THEN '🥬' -- Spinach
    ELSE '🍽️'
END
WHERE id IN (
    1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,
    106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,
    122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,
    138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,
    154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,
    170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,
    186,187
);