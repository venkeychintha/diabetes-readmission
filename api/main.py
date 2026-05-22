import time
from fastapi import FastAPI, HTTPException
from api.schemas import PatientRecord, PredictionResponse
from api.predictor import load_model, predict

app = FastAPI(
    title="Diabetes Readmission Prediction API",
    description="Predicts 30-day hospital readmission risk for diabetic patients.",
    version="1.0.0"
)

model, features, version = load_model()


@app.get("/health")
def health():
    return {"status": "ok", "model_version": version}


@app.post("/predict", response_model=PredictionResponse)
def predict_readmission(record: PatientRecord):
    try:
        start = time.time()
        prob, label = predict(record.model_dump(), model, features)
        latency_ms = (time.time() - start) * 1000
        print(f"Inference latency: {latency_ms:.2f}ms")
        return PredictionResponse(
            readmitted_within_30_days=label,
            probability=round(prob, 4),
            model_version=version
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
