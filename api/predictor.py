import joblib
import pandas as pd
import os
import glob


def get_latest_artifact_dir(artifact_base: str = "artifacts") -> str:
    dirs = sorted(glob.glob(os.path.join(artifact_base, "v_*")))
    if not dirs:
        raise FileNotFoundError("No model artifacts found. Run training first.")
    return dirs[-1]


def load_model(artifact_dir: str = None):
    if artifact_dir is None:
        artifact_dir = get_latest_artifact_dir()
    model = joblib.load(os.path.join(artifact_dir, "model.pkl"))
    features = joblib.load(os.path.join(artifact_dir, "features.pkl"))
    version = os.path.basename(artifact_dir)
    return model, features, version


def predict(record: dict, model, features: list) -> tuple[float, bool]:
    df = pd.DataFrame([record])

    # encode categoricals
    cat_cols = df.select_dtypes(include="object").columns.tolist()
    df[cat_cols] = df[cat_cols].astype(str)
    df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

    # align to training features
    df = df.reindex(columns=features, fill_value=0)

    prob = model.predict_proba(df)[0][1]
    label = bool(prob >= 0.5)
    return prob, label
