# ⚽ LaLiga Match Predictor

A data science project focused on building an end-to-end football analytics pipeline using LaLiga match data. The goal is to collect, process, analyze, and eventually predict football match outcomes using machine learning models.

---

## 📌 Project Overview

This project simulates a real-world data science workflow, covering:

- Data extraction from a public football API
- Data cleaning and transformation
- Exploratory Data Analysis (EDA)
- Feature engineering (future phase)
- Machine learning modeling (future phase)
- Dashboard visualization (Power BI / future integration)
- Automated data updates (future phase)

The project is designed as a progressive learning system, where each stage builds toward a complete data product.

---

## 🧠 Current Status (Phase 2: Early Analytics & Foundation Building)

We have moved beyond initial data ingestion and are now building early analytical structures on top of the dataset. The focus is shifting from raw data handling to transforming match data into analytical and model-ready formats.

### ✅ Completed so far:
- Connection to Football-Data API
- Extraction of LaLiga match data
- Parsing nested JSON structures
- Creation of structured dataset using pandas
- Selection of relevant variables:
  - Match ID
  - Date
  - Season
  - Matchday
  - Home / Away teams
  - Goals
  - Winner
  - Match status
- Conversion of raw JSON into a structured DataFrame
- Basic data type cleaning (e.g. datetime conversion)
- Creation of team standings (league table) from match data

### 📊 Output so far:
A structured dataset of ~380 matches per season stored in a DataFrame and exported as CSV.

---

## 🏗️ Project Structure

```
Laliga-match-predictor/
│
├── data/                # Raw and processed datasets
├── src/                 # Main Python scripts
│   └── get_matches.py   # API extraction script
├── notebooks/           # Exploratory analysis notebooks
├── models/              # Future ML models
├── dashboard/           # Power BI / visualization layer
├── .env                 # API keys (not tracked in git)
├── .gitignore
└── README.md
```

---

## 🚀 Next Steps

The project will evolve through the following stages:

### 🟡 Phase 2: Exploratory Data Analysis (EDA)
- Match result distribution
- Home vs away performance
- Goal statistics
- Seasonal trends
- Data quality checks

---

### 🟠 Phase 3: Feature Engineering
We will build predictive features such as:
- Team form (last N matches)
- Average goals scored/conceded
- Home/away performance strength
- Rolling statistics
- Temporal trends

---

### 🔴 Phase 4: Machine Learning Model
Initial models will focus on:
- Predicting match outcome:
  - Home win
  - Draw
  - Away win
- Probability-based predictions
- Baseline models (Logistic Regression, Random Forest, etc.)

---

### 🟣 Phase 5: Dashboard (Power BI / Visualization)
- Interactive dashboard
- Match trends over time
- Team performance comparisons
- Model predictions visualization

---

### ⚫ Phase 6: Automation & Scaling
- Daily/weekly API data updates
- Automatic dataset refresh
- Model retraining pipeline
- Expansion to multiple leagues (Premier League, Serie A, etc.)

---

## 🎯 Project Goals

This project is not just about football prediction, but about learning a full data science workflow:

- Working with real-world APIs
- Handling raw, nested data
- Building reproducible data pipelines
- Applying statistical and ML methods
- Creating visual and interpretable outputs

---

## 🛠️ Tech Stack

- Python
- Pandas
- Requests
- Scikit-learn (future)
- Power BI
- Football-Data API
- Git & GitHub

---

## 📈 Long-Term Vision

The final goal is to build a complete football analytics system capable of:

- Continuously updating match data
- Generating insights in real time
- Predicting match outcomes probabilistically
- Visualizing team performance evolution over time

---

## ⚠️ Notes

- API key is stored securely using `.env`
- Project is under active development
- Structure and features will evolve over time

---

## 👨‍💻 Author

Data Science and Engineering student focused on machine learning, data analytics, and applied AI in real-world systems.

