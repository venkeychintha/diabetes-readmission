# Diabetes 30-Day Readmission Prediction Service

Binary classification system that predicts whether a patient will be readmitted
within 30 days, built on the UCI Diabetes 130-US Hospitals dataset.

---

## Project Structure

    diabetes-readmission/
    ├── src/
    │   ├── data/        # data loading & preprocessing
    │   ├── features/    # feature engineering
    │   ├── models/      # training & evaluation
    │   └── utils/       # helpers
    ├── api/             # FastAPI inference service
    ├── configs/         # YAML config files
    ├── tests/           # unit + integration tests
    ├── scripts/         # CLI entry points
    ├── artifacts/       # saved models (gitignored)
    ├── data/raw/        # raw dataset (gitignored)
    ├── docs/            # design docs
    ├── Dockerfile
    ├── docker-compose.yml
    └── requirements.txt

---

## Setup

### Step 1 - Initialize Project Structure

1. Created main project folder: diabetes-readmission
2. Created subfolders: src/data, src/features, src/models, src/utils, api, configs, tests, scripts, artifacts, data/raw, docs
3. Created __init__.py files in all Python module folders
4. Created placeholder files: README.md, requirements.txt, Dockerfile, docker-compose.yml, .gitignore
5. Initialized git repository

### Step 2 - Download Dataset

Dataset: Diabetes 130-US Hospitals (UCI)
Source: https://archive.ics.uci.edu/ml/datasets/diabetes+130-us+hospitals+for+years+1999-2008

Install the download package:

    pip install ucimlrepo

Download the dataset:

    python scripts/download_data.py

This saves raw data to data/raw/diabetic_data.csv
Records: 101,766 rows x 48 columns

Note: data/raw/ is gitignored. Run this command after every fresh clone.

---

## Train

Coming soon

---

## Evaluate

Coming soon

---

## Serve

Coming soon

---

## Test

Coming soon

---

## Limitations

To be documented

---

## Improvements

To be documented
