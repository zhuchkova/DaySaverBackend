INSERT INTO gi_categories (name) VALUES
('low'),
('medium'),
('high')
ON CONFLICT (name) DO NOTHING;