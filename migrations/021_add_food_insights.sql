CREATE TABLE food_insights (
    food_id BIGINT PRIMARY KEY REFERENCES foods(id) ON DELETE CASCADE,
    short_label TEXT,
    theme TEXT,
    headline TEXT,
    subtitle TEXT,
    body TEXT,
    effects JSONB,
    warning_title TEXT,
    warning_body TEXT,
    education_title TEXT,
    education_body TEXT,
    highlight_title TEXT,
    highlight_points JSONB
);