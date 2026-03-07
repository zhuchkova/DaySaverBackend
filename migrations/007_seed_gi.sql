INSERT INTO gi (food_id, value, gi_category_id, data_source)
VALUES
(1, 55, 2, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(2, 56, 2, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(3, 69, 2, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(4, 74, 3, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(5, 79, 3, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(6, 81, 3, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(7, 51, 1, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(8, 75, 3, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(9, 95, 3, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(10, 31, 1, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(11, 31, 1, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(12, 33, 1, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(13, 33, 1, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(14, 40, 1, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(15, 44, 1, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(16, 38, 1, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(17, 41, 1, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(18, 50, 1, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(19, 13, 1, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(20, 22, 1, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(21, 15, 1, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(22, 39, 1, 'Glycemic Index Chart, Arkansas Heart Hospital'),
(23, 22, 1, 'Glycemic Index Chart, Arkansas Heart Hospital')

ON CONFLICT (food_id) DO NOTHING;