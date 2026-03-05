CREATE INDEX idx_foods_category_id    ON foods (category_id);
CREATE INDEX idx_gi_gi_category_id    ON gi (gi_category_id);
CREATE INDEX idx_portions_food_id     ON portions (food_id);
CREATE INDEX idx_recipes_category_id  ON recipes (category_id);


CREATE INDEX idx_rim_food_id          ON recipes_ingredients_mapping (food_id);