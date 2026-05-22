# Design Rationale

## Repository Structure
The project follows a clean separation of concerns:
- `src/` contains all core ML logic (data, features, models, utils)
- `api/` contains the FastAPI inference service
- `tests/` contains all automated tests
- `scripts/` contains CLI entry points for training
- `configs/` reserved for YAML configuration files
- `artifacts/` stores versioned model artifacts (gitignored)

This structure ensures that the ML pipeline and the serving layer
are decoupled. A team member can retrain the model without touching
the API code, and the API can be updated without retraining.

## Model Choice — Logistic Regression
We chose Logistic Regression over more complex models (Random Forest,
XGBoost) for the following reasons:
- Fast training and inference (well within 250ms p95 latency target)
- Interpretable coefficients — important in healthcare-adjacent settings
- Works well with class imbalance using `class_weight="balanced"`
- Easier to audit and explain during clinical review

A StandardScaler pipeline is used to normalize features before
passing them to the model, ensuring training/inference parity.

## Artifact Strategy
Model artifacts are versioned using timestamps (e.g. `v_20260521_183933`).
Each version folder contains:
- `model.pkl` — the trained pipeline (scaler + classifier)
- `features.pkl` — the exact feature list used during training

The API always loads the latest artifact at startup. This makes
rollback straightforward — simply remove the latest folder and
restart the service.

## API Design
FastAPI was chosen because:
- Auto-generates OpenAPI/Swagger documentation
- Pydantic v2 handles request/response validation automatically
- Async-capable for future scalability
- Lightweight and production-proven

All inputs are validated via Pydantic schemas before reaching the
model. Missing fields default to safe values matching the training
distribution.

## Training/Inference Parity
The same preprocessing logic (encoding, column alignment) is applied
at both training and inference time. The feature list saved in
`features.pkl` is used to reindex inference inputs — ensuring no
feature mismatch between training and serving.

## Trade-offs
- Logistic Regression sacrifices some accuracy for interpretability
- Timestamp versioning is simple but not as robust as MLflow Model Registry
- One-hot encoding at inference time is stateless but requires
  careful alignment with training features
- Docker image is large (~1GB) due to ML dependencies
