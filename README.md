<<<<<<< HEAD
# Diabetes 30-Day Readmission Prediction Service

Binary classification system that predicts whether a diabetic patient
will be readmitted to hospital within 30 days.

Built on the UCI Diabetes 130-US Hospitals dataset (1999-2008).

---

## Project Structure

    diabetes-readmission/
    ├── src/
    │   ├── data/           # data loading & preprocessing
    │   ├── features/       # feature engineering
    │   ├── models/         # training & evaluation
    │   └── utils/          # helpers
    ├── api/                # FastAPI inference service
    ├── configs/            # YAML configuration files
    ├── tests/              # automated tests
    ├── scripts/            # CLI entry points
    ├── artifacts/          # versioned model artifacts (gitignored)
    ├── data/raw/           # raw dataset (gitignored)
    ├── docs/               # design docs, model card, assumption log
    ├── Dockerfile
    ├── docker-compose.yml
    ├── requirements.txt
    └── setup.py

---

## Setup

### 1. Clone the repository
    git clone <repo-url>
    cd diabetes-readmission

### 2. Create and activate virtual environment
    python -m venv venv
    venv\Scripts\activate        # Windows
    source venv/bin/activate     # Mac/Linux

### 3. Install dependencies
    pip install -r requirements.txt

### 4. Install project as editable package
    pip install -e .

---

## Data Access

Dataset: Diabetes 130-US Hospitals (UCI)
Source: https://archive.ics.uci.edu/ml/datasets/diabetes+130-us+hospitals+for+years+1999-2008

Download the dataset by running:

    python scripts/download_data.py

This saves raw data to data/raw/diabetic_data.csv
Records: 101,766 rows x 48 columns

Note: data/raw/ is gitignored. Run this command after every fresh clone.

---

## Train

Run the training pipeline:

    python scripts/train.py

Optional arguments:

    python scripts/train.py --data data/raw/diabetic_data.csv --artifacts artifacts

This will:
- Load and preprocess the dataset
- Train a Logistic Regression model with balanced class weights
- Log metrics and parameters to MLflow
- Save versioned model artifacts to artifacts/v_YYYYMMDD_HHMMSS/

View MLflow experiment tracking UI:

    mlflow ui

Then open: http://127.0.0.1:5000

---

## Evaluate

Model performance on test set (80/20 split):

| Metric         | Value  |
|----------------|--------|
| ROC-AUC        | 0.6713 |
| F1 Score       | 0.2728 |
| Recall (class 1) | 0.54 |
| Accuracy       | 0.68   |

---

## Serve

### Option A — Run locally

    uvicorn api.main:app --reload --port 8000

### Option B — Run with Docker

    docker build -t diabetes-readmission .
    docker run -p 8000:8000 diabetes-readmission

### Option C — Run with Docker Compose

    docker-compose up

API will be available at:
- Swagger UI: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health
- Predict: POST http://127.0.0.1:8000/predict

Example request:

    curl -X POST http://127.0.0.1:8000/predict \
      -H "Content-Type: application/json" \
      -d '{"race": "Caucasian", "gender": "Male", "age": "[70-80)",
           "time_in_hospital": 3, "num_medications": 15}'

Example response:

    {
      "readmitted_within_30_days": false,
      "probability": 0.0069,
      "model_version": "v_20260521_183933"
    }

---

## Test

Run all automated tests:

    pytest tests/ -v

Tests cover:
- API endpoints (health check, predict, invalid input, empty input)
- Model loading and prediction output validation
- Preprocessing functions (cleaning, encoding, target creation)

---

## Limitations

- Trained on 1999-2008 data — clinical practices have changed since then
- ICD diagnosis codes excluded due to high cardinality
- Fairness evaluation across demographic subgroups not performed
- High false positive rate — low precision for readmission class
- Not validated in a real clinical environment

---

## Improvements With More Time

- Group ICD diagnosis codes by disease category
- Tune classification threshold using precision-recall curve
- Perform fairness audit across race, gender, age subgroups
- Add SHAP values for prediction explainability
- Replace timestamp versioning with MLflow Model Registry
- Add input drift detection for production monitoring
- Store artifacts in cloud object storage (S3/GCS)
- Add CI/CD pipeline with GitHub Actions
=======
# diabetes-readmission
>>>>>>> bec8ef7f9cc6032ac5334b02d7377584c7627503
