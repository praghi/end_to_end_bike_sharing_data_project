import os 

## ...............................
# Define project folder structure
## ............................... 
folders = [
    "business_intelligence/data/bronze",
    "business_intelligence/data/silver",
    "business_intelligence/data/gold",
    "business_intelligence/visualization/powerbi",
    "business_intelligence/src/ingestion",
    "business_intelligence/src/transformation",
    "business_intelligence/src/utils",
    "business_intelligence/logs",

    "machine_learning/src/feature_engineering",
    "machine_learning/src/training",
    "machine_learning/src/evaluation",
    "machine_learning/src/inference",
    "machine_learning/src/utils",
    "machine_learning/artifacts",
    "machine_learning/logs",

    "app/streamlit_app",
    "app/fastapi_app",

    "config",
    "notebooks",
    ".github/workflows"
]

files = [
    "business_intelligence/src/utils/logger.py",
    "business_intelligence/logs/bi_pipeline.log",
    "business_intelligence/dvc.yaml",

    "machine_learning/src/utils/logger.py",
    "machine_learning/logs/ml_pipeline.log",
    "machine_learning/dvc.yaml",

    "app/streamlit_app/app.py",
    "app/fastapi_app/main.py",

    "config/config.yaml",
    ".github/workflows/cicd.yml",
    "notebooks/bi_pipeline.ipynb",
    "notebooks/ml_pipeline.ipynb",
    "requirements.txt",
    "README.md",
    "LICENSE",
    ".gitignore",
    ".dvcignore"
]

# ------------------------------
# Create folders and files  
# ------------------------------ 

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder} ")

for file_path in files:
    # Create empty file if not exists
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            pass
        print(f"File created: {file_path}")
    else:
        print(f"File exists, skipped: {file_path}")

print("\n Project structure setup complete!")