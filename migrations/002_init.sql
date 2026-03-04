CREATE TABLE categories (
  id BIGSERIAL PRIMARY KEY,
  name TEXT NOT NULL UNIQUE
);

CREATE TABLE gi_categories (
  id BIGSERIAL PRIMARY KEY,
  name TEXT NOT NULL UNIQUE
);

CREATE TABLE foods (
  id BIGSERIAL PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  source_name TEXT,
  description TEXT,
  category_id BIGINT REFERENCES categories(id),
  data_source TEXT,
  fdc_id TEXT,
  kcal_per_100g REAL,
  protein_g_per_100g REAL,
  fat_g_per_100g REAL,
  carbs_g_per_100g REAL,
  fiber_g_per_100g REAL,
  sugars_g_per_100g REAL
);

CREATE TABLE gi (
  food_id BIGINT PRIMARY KEY REFERENCES foods(id) ON DELETE CASCADE,
  value INT NOT NULL,
  gi_category_id BIGINT NOT NULL REFERENCES gi_categories(id),
  data_source TEXT
);

CREATE TABLE portions (
  id BIGSERIAL PRIMARY KEY,
  value TEXT NOT NULL,
  unit_name TEXT NOT NULL,
  gram_weight REAL NOT NULL,
  food_id BIGINT NOT NULL REFERENCES foods(id)
);

CREATE TABLE recipes (
  id BIGSERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  category_id BIGINT REFERENCES categories(id),
  description TEXT
);

CREATE TABLE recipes_ingredients_mapping (
  recipe_id BIGINT NOT NULL REFERENCES recipes(id) ON DELETE CASCADE,
  food_id BIGINT NOT NULL REFERENCES foods(id),
  default_grams REAL NOT NULL,
  PRIMARY KEY (recipe_id, food_id)
);