# DaySaver Backend

The **DaySaver Backend** is the core engine powering a smart breakfast assistant that transforms food data into **actionable health insights**.

It processes meals, evaluates their metabolic impact, and returns structured recommendations that help users make better food choices.

---

## 🚀 Main Features

* 🥗 **Meal Analysis**

  * Aggregates macronutrients (protein, fat, carbs)
  * Calculates **glycemic load** and spike risk
  * Computes **satiety score**

* 📊 **Health Insights**

  * Energy level prediction
  * Hunger & satiety feedback
  * Ingredient-level explanations

* 🔁 **Smart Recommendations**

  * Suggests healthier swaps
  * Diet-aware logic (e.g., vegan-friendly alternatives)

* 📸 **Image-Based Detection (Experimental)**

  * Detect breakfast items from uploaded images
  * Map detected foods to internal database (RAG-based approach)

---

## 🏗️ Tech Stack

* **Framework:** FastAPI
* **Database:** PostgreSQL (Supabase)
* **Deployment:** Render
* **Architecture:** Modular services (analysis, recommendations, detection)

---

## 📡 API Endpoints

### Core Endpoints

* `GET /api/v1/catalog`
  → Get full food catalog with portions

* `GET /api/v1/foods/search`
  → Search foods

* `GET /api/v1/foods/{food_id}/portions`
  → Get portion options

* `GET /api/v1/foods/{food_id}/insight`
  → Educational insights for a food

---

### 🧠 Analysis

* `POST /api/v1/analyze`
  → Main endpoint for meal evaluation

**What it does:**

* Aggregates macros
* Computes glycemic impact
* Calculates satiety
* Returns recommendations & swaps

---

### 📷 Image Detection

* `POST /api/v1/detect-from-image`
  → Detect breakfast items from an image

**Flow:**

1. Upload image
2. Model detects foods
3. Maps results to internal `food_id`, `portion_id`
4. Returns candidates for analysis

---

## 🗂️ Project Structure

```
backend/
├── migrations/            # DB migrations (SQL)
├── schemas/               # API models
├── services/              # Core business logic
│   ├── analyze.py         # Recommendation service 
│   └── image_detection.py # Image detection service
├── scripts/               # DB migration script
├── tests/                 # Unit tests
├── main.py                # FastAPI entry point
└── requirements.txt
```

---

## ⚙️ Running Locally

```bash
# create virtual env
python -m venv .venv
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run server
uvicorn main:app --reload
```

---

## 🌍 Deployment

The backend is deployed on Render:

👉 [https://daysaverbackend.onrender.com/docs](https://daysaverbackend.onrender.com/docs)

Interactive Swagger UI available for testing endpoints.

---

## ⚠️ Limitations (Free Tier Usage)

**This project is deployed using free-tier services, which may introduce some constraints:**

* **Render (Backend Hosting)**

    The backend runs on a free Render instance.
    
    👉 “Your free instance will spin down with inactivity, which can delay requests by 50 seconds or more.”
    
    This means the first request after inactivity may be slow.
* **Gemini Flash 2.5 API (Image Detection)**

    We use the free tier of the Gemini API, which includes rate limits.
    * → Requests may fail or be throttled if limits are exceeded
    * → See official limits: https://ai.google.dev/gemini-api/docs/rate-limits

* **Supabase (Database)**

    The database is hosted on a free Supabase instance, which may result in:
    * Slower query performance under load
    * Possible cold starts or temporary unavailability

💡 These limitations are expected in a prototype environment and can be resolved by upgrading to paid plans.

---

## 📌 Design Principles

* **UX-driven backend** → responses tailored for frontend rendering
* **Structured outputs** → no raw data, only meaningful insights
* **Separation of concerns** → data, logic, and presentation layers
* **Extensibility** → ready for personalization & ML integration

---

## 🤝 Summary

The backend transforms complex nutrition data into **clear, actionable guidance**, enabling users to understand not just *what* they eat but *how it affects them*.

