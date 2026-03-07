INSERT INTO portions (label, unit_name, gram_weight, food_id, display_order) VALUES

-- OATMEAL
('small bowl', 'bowl', 150, 1, 1),
('medium bowl', 'bowl', 220, 1, 2),
('large bowl', 'bowl', 300, 1, 3),

-- MUESLI
('small bowl', 'bowl', 40, 2, 1),
('medium bowl', 'bowl', 60, 2, 2),
('large bowl', 'bowl', 80, 2, 3),

-- SPECIAL K
('small bowl', 'bowl', 30, 3, 1),
('medium bowl', 'bowl', 45, 3, 2),
('large bowl', 'bowl', 60, 3, 3),

-- CHEERIOS
('small bowl', 'bowl', 30, 4, 1),
('medium bowl', 'bowl', 45, 4, 2),
('large bowl', 'bowl', 60, 4, 3),

-- INSTANT OATMEAL
('small bowl', 'bowl', 150, 5, 1),
('medium bowl', 'bowl', 220, 5, 2),
('large bowl', 'bowl', 300, 5, 3),

-- CORNFLAKES
('small bowl', 'bowl', 25, 6, 1),
('medium bowl', 'bowl', 40, 6, 2),
('large bowl', 'bowl', 55, 6, 3),

-- WHOLE GRAIN BREAD
('1 slice', 'slice', 35, 7, 1),
('2 slices', 'slice', 70, 7, 2),
('3 slices', 'slice', 105, 7, 3),

-- WHITE BREAD
('1 slice', 'slice', 30, 8, 1),
('2 slices', 'slice', 60, 8, 2),
('3 slices', 'slice', 90, 8, 3),

-- BAGUETTE
('1 slice', 'slice', 25, 9, 1),
('2 slices', 'slice', 50, 9, 2),
('3 slices', 'slice', 75, 9, 3),

-- WHOLE MILK
('small cup', 'cup', 150, 10, 1),
('medium cup', 'cup', 250, 10, 2),
('large cup', 'cup', 350, 10, 3),

-- SKIM MILK
('small cup', 'cup', 150, 11, 1),
('medium cup', 'cup', 250, 11, 2),
('large cup', 'cup', 350, 11, 3),

-- SWEETENED YOGURT
('small cup', 'cup', 125, 12, 1),
('medium cup', 'cup', 175, 12, 2),
('large cup', 'cup', 250, 12, 3),

-- LOW FAT YOGURT
('small cup', 'cup', 125, 13, 1),
('medium cup', 'cup', 175, 13, 2),
('large cup', 'cup', 250, 13, 3),

-- CHOCOLATE MILK
('small cup', 'cup', 150, 14, 1),
('medium cup', 'cup', 250, 14, 2),
('large cup', 'cup', 350, 14, 3),

-- SOY MILK
('small cup', 'cup', 150, 15, 1),
('medium cup', 'cup', 250, 15, 2),
('large cup', 'cup', 350, 15, 3),

-- TOMATO JUICE
('small glass', 'glass', 150, 16, 1),
('medium glass', 'glass', 250, 16, 2),
('large glass', 'glass', 350, 16, 3),

-- APPLE JUICE
('small glass', 'glass', 150, 17, 1),
('medium glass', 'glass', 250, 17, 2),
('large glass', 'glass', 350, 17, 3),

-- ORANGE JUICE
('small glass', 'glass', 150, 18, 1),
('medium glass', 'glass', 250, 18, 2),
('large glass', 'glass', 350, 18, 3),

-- PEANUTS
('1 tbsp', 'tbsp', 10, 19, 1),
('2 tbsp', 'tbsp', 20, 19, 2),
('3 tbsp', 'tbsp', 30, 19, 3),

-- CASHEWS
('1 tbsp', 'tbsp', 10, 20, 1),
('2 tbsp', 'tbsp', 20, 20, 2),
('3 tbsp', 'tbsp', 30, 20, 3),

-- TOMATO
('small portion', 'portion', 50, 21, 1),
('medium portion', 'portion', 100, 21, 2),
('large portion', 'portion', 150, 21, 3),

-- CARROTS
('small portion', 'portion', 50, 22, 1),
('medium portion', 'portion', 100, 22, 2),
('large portion', 'portion', 150, 22, 3),

-- CHERRIES
('small bowl', 'bowl', 75, 23, 1),
('medium bowl', 'bowl', 150, 23, 2),
('large bowl', 'bowl', 225, 23, 3)

ON CONFLICT (food_id, display_order) DO NOTHING;
