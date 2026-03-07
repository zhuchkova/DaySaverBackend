INSERT INTO categories (name) VALUES
('Cereals'),
('Bread and Bakery'),
('Dairy'),
('Eggs'),
('Fruits'),
('Vegetables'),
('Nuts and Seeds'),
('Plant Proteins'),
('Meat'),
('Fish'),
('Fats and Oils'),
('Sweeteners'),
('Beverages'),
('Snack Foods'),
('Grains and Starches')
ON CONFLICT (name) DO NOTHING;


