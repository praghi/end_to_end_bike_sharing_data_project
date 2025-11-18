# 🚴 PedalBreeze — End-to-End Bike Demand Analytics Data Project 

# Project Overview

PedalBreeze is a fictitious bike-sharing startup headquartered in Washington DC, USA.
After two years of operations, the company has collected a significant amount of rider usage data, but lacks the analytical capability to transform it into meaningful business insights.

This project simulates how a  real life Data Scientists builds a complete end-to-end analytics platform to support executive decision-making and scalability.

The project is built around three major pillars divided into II phases :

## PHASE I
 # 1. Business Intelligence & Data Engineering
🔹 Ingestion | Transformation Layer 

- Source data stored in Azure Blob Storage
- Secure authentication using env and GitHub Secrets
- Incremental ingestion based on (work in progress):
   - Row count comparison
   - Max ID logic 
-  Validation (schema, emptiness, file existence) 
- Raw files stored in bronze folder   
- Clean and Transformed data silver folder

# 2. Analytics & Power BI Dashboard

The Gold layer powers the PedalBreeze BI Dashboard, answering key business questions:
- Total Demand vs Expected Demand Trend
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

## Power BI File Path :  
  - [Dashboard pbi path](https://github.com/praghi/end_to_end_bike_sharing_data_project/tree/main/business_intelligence/visualization/powerbi)
  - [Measures List](https://github.com/praghi/end_to_end_bike_sharing_data_project/tree/main/business_intelligence/visualization/powerbi) 
  - [Useful Icons](https://github.com/praghi/end_to_end_bike_sharing_data_project/tree/main/icons)

## PHASE II

# 3. Machine Learning + Streamlit MVP App

PedalBreeze aims to forecast hourly bike demand using inputs such as:

- Temperature
- Weather category
- Hour of day
- Seasons
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

# Technical Flow Chart   
  - [Docs](https://github.com/praghi/end_to_end_bike_sharing_data_project/tree/main/docs)
  ![Tech Diagram](https://github.com/praghi/end_to_end_bike_sharing_data_project/blob/main/icons/PedalBreezeBikeSharing_Technical_Flow_Chart.png)
  ![ProjectStructure] (https://github.com/praghi/end_to_end_bike_sharing_data_project/blob/main/docs/Project_Snapshot.png)


# Notebooks 
- [BI Pipeline](https://github.com/praghi/end_to_end_bike_sharing_data_project/tree/main/docs) 
- [ML Pipeline](https://github.com/praghi/end_to_end_bike_sharing_data_project/blob/main/notebooks/ml_pipeline.ipynb)


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

# To do list 

- ML Bikesharing Predictive Model 
- Modular coding design 
- Streamlit Front-end App  
- DVC Version Control 
- ML Flow Tracking 
- FastAPI (optional)


# Data Credit, License & Performance Measurement 
- UCI Machine Learning Dataset : https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset   
- To ensure our modeling pipeline meets industry-level quality, the project also references Kaggle’s competitive ecosystem. Aim towards achieving a Top 1% percentile ranking against challengers.