# 🚴 PedalBreeze — End-to-End Bike Demand Analytics Data Project 

# Project Overview

PedalBreeze is a fictitious bike-sharing startup headquartered in LA, USA.
After two years of operations, the company has collected a significant amount of rider usage data, but lacks the analytical capability to transform it into meaningful business insights.

This project simulates how a  real life Data Scientists builds a complete end-to-end analytics platform to support executive decision-making and scalability.

The project is built around three major pillars:

 # 1. Business Intelligence & Data Engineering
🔹 Ingestion | Transformation Layer 

- Source data stored in Azure Blob Storage
- Secure authentication using env and GitHub Secrets
- Incremental ingestion based on:
   - Row count comparison
   - Max ID logic ( To be implemented)
   - Validation (schema, emptiness, file existence) 
   - Raw files stored in bronze folder   
   - Clean and Transformed data silver folder

# 2. Analytics & Power BI Dashboard

The Gold layer powers the PedalBreeze BI Dashboard, answering key business questions:
- Total Demand vs Expected Trend
- Median Daily Demand
- Hourly demand patterns (0–23)
- Seasonal ridership behaviour
- Weather impact on usage
- Temperature correlation with demand
- Quarterly demand movement

The dashboard showcases:
- Star schema modelling
- Measures (DAX) for all KPI
- KPI cards, time-series graphs, heatmaps
- Slicers for season, weather, date range

## Power BI File Path : https://github.com/praghi/end_to_end_bike_sharing_data_project/tree/develop/business_intelligence/visualization/powerbi 

# 3. Machine Learning + Streamlit MVP App

PedalBreeze aims to forecast hourly bike demand using inputs such as:

- Temperature
- Weather category
- Hour of day
- Season
- Humidity & windspeed

The ML workflow includes:

- Explotary Data Analysis (EDA) 
- Feature engineering
- Train/test split
- Model training (Linear Regression, SVM, Random Forest, XGBoost etc.)
- Evaluation metrics : (MSE, RMSE, ARMSE) 
- Model Deployment 

a) Saving model artifacts into /machine_learning/artifacts/  
b) Simple Streamlit MVP App for real-time predictions  
c) Tracing of ML model using mlflow using dagshub (work in progress)

### The app allows business users to simulate “what-if scenarios” and plan fleet allocation.

# Governance, CI/CD, and Version Control

This project follows enterprise-grade engineering standards:

- Secure Secrets
- Azure credentials stored in GitHub Actions Secrets
- No .env files in repo
- Version Control
- Branching strategy: main, develop/*
- CI/CD with GitHub Actions 
- All development done in develop → CI → Pull Request
- Logging & Utils 
- Metadata tracking 
- Modular coding
- Incremental processes ensure idempotent runs (To be implemented)
- Logs stored under BI and ML modules

# Data Credit, License & Performance Measurement 
UCI Machine Learning Dataset : https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset 
To ensure our modeling pipeline meets industry-level quality, the project also references Kaggle’s competitive ecosystem. Aim towards achieving a Top 1% percentile ranking against challengers.


## 🛠️ Installation

Clone repo:
```bash
git clone https://github.com/praghi/end_to_end_bike_sharing_data_project.git
``` 

Create virtual environment (using uv): 
```bash
uv venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

Install dependencies: 
```bash
uv pip install -r requirements.txt
```   