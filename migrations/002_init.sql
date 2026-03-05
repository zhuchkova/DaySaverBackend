CREATE TABLE categories (
  id   BIGSERIAL PRIMARY KEY,
  name TEXT      NOT NULL UNIQUE
);

CREATE TABLE gi_categories (
   id   BIGSERIAL  PRIMARY KEY,
   name TEXT       NOT NULL UNIQUE
);

CREATE TABLE foods (
   id                  BIGSERIAL      PRIMARY KEY,
   name                TEXT           NOT NULL UNIQUE,
   source_name         TEXT,
   description         TEXT,
   category_id         BIGINT         REFERENCES categories(id) ON DELETE SET NULL,
   data_source         TEXT,
   fdc_id              TEXT           UNIQUE,
   kcal_per_100g       NUMERIC(8, 2)  CHECK (kcal_per_100g       >= 0),
   protein_g_per_100g  NUMERIC(8, 4)  CHECK (protein_g_per_100g  >= 0),
   fat_g_per_100g      NUMERIC(8, 4)  CHECK (fat_g_per_100g      >= 0),
   carbs_g_per_100g    NUMERIC(8, 4)  CHECK (carbs_g_per_100g    >= 0),
   fiber_g_per_100g    NUMERIC(8, 4)  CHECK (fiber_g_per_100g    >= 0),
   sugars_g_per_100g   NUMERIC(8, 4)  CHECK (sugars_g_per_100g   >= 0)
);

CREATE TABLE gi (
   food_id         BIGINT  PRIMARY KEY REFERENCES foods(id) ON DELETE CASCADE,
   value           INT     NOT NULL CHECK (value BETWEEN 0 AND 100),
   gi_category_id  BIGINT  NOT NULL REFERENCES gi_categories(id) ON DELETE RESTRICT,
   data_source     TEXT
);

CREATE TABLE portions (
   id           BIGSERIAL      PRIMARY KEY,
   label        TEXT           NOT NULL,
   unit_name    TEXT           NOT NULL,
   gram_weight  NUMERIC(8, 2)  NOT NULL CHECK (gram_weight > 0),
   food_id      BIGINT         NOT NULL REFERENCES foods(id) ON DELETE CASCADE
);

CREATE TABLE recipes (
   id           BIGSERIAL  PRIMARY KEY,
   name         TEXT       NOT NULL UNIQUE,
   category_id  BIGINT     REFERENCES categories(id) ON DELETE SET NULL,
   description  TEXT
);

CREATE TABLE recipes_ingredients_mapping (
   recipe_id     BIGINT         NOT NULL REFERENCES recipes(id) ON DELETE CASCADE,
   food_id       BIGINT         NOT NULL REFERENCES foods(id)   ON DELETE RESTRICT,
   default_grams NUMERIC(8, 2)  NOT NULL CHECK (default_grams > 0),
   PRIMARY KEY (recipe_id, food_id)
);