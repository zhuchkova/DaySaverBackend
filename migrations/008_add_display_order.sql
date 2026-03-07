ALTER TABLE portions
ADD COLUMN display_order INT NOT NULL;

ALTER TABLE portions
ADD CONSTRAINT unique_food_portion_order
UNIQUE (food_id, display_order);