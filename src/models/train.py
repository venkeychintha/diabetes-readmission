import joblib
import mlflow
import mlflow.sklearn
import os
from datetime import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.metrics import (
    classification_report,
    roc_auc_score,
    f1_score
)

from src.data.preprocess import run_pipeline


def train(data_path: str, artifact_dir: str = "artifacts"):
    X_train, X_test, y_train, y_test = run_pipeline(data_path)

    version = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_dir = os.path.join(artifact_dir, f"v_{version}")
    os.makedirs(save_dir, exist_ok=True)

    mlflow.set_experiment("diabetes-readmission")

    with mlflow.start_run():
        model = Pipeline([
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(
                class_weight="balanced",
                max_iter=1000,
                random_state=42,
                n_jobs=-1
            ))
        ])


        print("Training model...")
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]

        roc_auc = roc_auc_score(y_test, y_prob)
        f1 = f1_score(y_test, y_pred)

        print(f"\nROC-AUC: {roc_auc:.4f}")
        print(f"F1 Score: {f1:.4f}")
        print(f"\n{classification_report(y_test, y_pred)}")

        mlflow.log_param("model_type", "LogisticRegression")
        mlflow.log_param("max_iter", 1000)
        mlflow.log_param("class_weight", "balanced")

        mlflow.log_metric("roc_auc", roc_auc)
        mlflow.log_metric("f1_score", f1)

        model_path = os.path.join(save_dir, "model.pkl")
        joblib.dump(model, model_path)

        feature_path = os.path.join(save_dir, "features.pkl")
        joblib.dump(list(X_train.columns), feature_path)

        mlflow.log_artifact(model_path)
        print(f"\nModel saved to: {save_dir}")

    return save_dir
