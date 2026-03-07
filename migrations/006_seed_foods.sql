INSERT INTO foods (name, source_name, description, category_id, data_source, fdc_id, kcal_per_100g, protein_g_per_100g, fat_g_per_100g, carbs_g_per_100g, fiber_g_per_100g, sugars_g_per_100g)
VALUES
('Oatmeal','Oatmeal','Oatmeal, multigrain',1,'Survey foods',2708398,56,2.12,0.46,12.19,2,0.41),
('Muesli','Muesli','MUESLI',1,'Branded foods',474366,392,9.6,7.9,62.9,7.1,31.4),
('Special K','Special K','Cereal, K''s, flavored',1,'Survey foods',2708472,363,7.33,1.15,80.94,8,28.38),
('Cheerios','Cheerios','Cereal, O''s, flavored',1,'Survey foods',2708446,385,8.62,5.37,75.99,7.6,32.35),
('Instant Oatmeal','Instant Oatmeal','Oatmeal, instant, plain, made with water, no added fat',1,'Survey foods',2708387,68,2.26,1.3,13.15,1.9,0.28),
('Cornflakes','Cornflakes','TOASTED GRAIN CEREAL, CORNFLAKES',1,'Branded foods',2477066,378,6.67,0,86.7,2.2,8.89),

('Whole Grain Bread','Whole Grain Bread','100% WHOLE GRAIN BREAD',2,'Branded foods',2083607,250,10.7,2.32,57.1,10.7,0),
('White Wheat Flour Bread','White Wheat Flour Bread','CLASSIC WHITE BREAD, CLASSIC WHITE',2,'Branded foods',2266405,289,7.89,3.95,52.6,2.6,2.63),
('Baguette, White, Plain','Baguette, White, Plain','Bread, French or Vienna, baguette, pre-sliced or not',2,'Survey foods',2707610,272,10.75,2.42,51.88,2.2,4.62),

('Whole Milk','Whole Milk','Milk, whole, 3.25% milkfat, with added vitamin D',3,'Foundation foods',746782,60,3.27,3.2,4.63,0,4.81),
('Skim Milk','Skim Milk','Milk, nonfat, fluid, with added vitamin A and vitamin D (fat free or skim)',3,'Foundation foods',746776,34,3.43,0.08,4.92,0,5.05),
('Sweetened Yogurt','Sweetened Yogurt','SWEETENED GREEK YOGURT, PLAIN',3,'Branded foods',1945716,73,8,2,13.3,0,5.33),
('Low Fat Yogurt','Low Fat Yogurt','Yogurt, Greek, plain, nonfat',3,'Foundation foods',330137,61,10.3,0.37,3.64,0,3.27),
('Chocolate Milk','Chocolate Milk','Chocolate milk, whole',3,'Survey foods',2705467,83,3.17,3.39,10.34,0.8,9.54),
('Soy Milk','Soy Milk','Soy milk, unsweetened, plain, shelf stable',3,'Foundation foods',1999630,38,3.55,2.12,1.29,0.4,0.56),

('Tomato Juice','Tomato Juice','Tomato juice, with added ingredients, from concentrate, shelf stable',13,'Foundation foods',2003596,23,0.86,0.29,4.32,0,2.57),
('Apple Juice, Unsweetened','Apple Juice, Unsweetened','Apple juice, with added vitamin C, from concentrate, shelf stable',13,'Foundation foods',2003590,48,0.09,0.29,11.4,0,10.3),
('Orange Juice, Unsweetened','Orange Juice, Unsweetened','Orange juice, no pulp, not fortified, from concentrate, refrigerated',13,'Foundation foods',2003591,47,0.73,0.32,10.3,0,8.28),

('Peanuts','Peanuts','Peanuts, raw',7,'Foundation foods',2515376,588,23.2,43.3,26.5,8,0),
('Cashews','Cashews','Nuts, cashew nuts, raw',7,'Foundation foods',2515374,565,17.4,38.9,36.3,4.1,0),

('Tomato','Tomato','Tomatoes, grape, raw',6,'Foundation foods',321360,27,0.83,0.63,5.51,2.1,0),
('Carrots','Carrots','Carrots, baby, raw',6,'Foundation foods',2258587,41,0.8,0.14,9.08,2.7,0),

('Cherries','Cherries','Cherries, sweet, dark red, raw',5,'Foundation foods',2346399,71,1.04,0.19,16.2,0,13.9)

ON CONFLICT (name) DO NOTHING;


