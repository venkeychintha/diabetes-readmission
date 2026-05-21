import pandas as pd
from sklearn.model_selection import train_test_split

COLS_TO_DROP = [
    "encounter_id", "patient_nbr",
    "examide", "citoglipton",
    "weight", "payer_code", "medical_specialty"
]

CATEGORICAL_COLS = [
    "race", "gender", "age", "admission_type_id",
    "discharge_disposition_id", "admission_source_id",
    "diag_1", "diag_2", "diag_3",
    "max_glu_serum", "A1Cresult",
    "metformin", "repaglinide", "nateglinide", "chlorpropamide",
    "glimepiride", "acetohexamide", "glipizide", "glyburide",
    "tolbutamide", "pioglitazone", "rosiglitazone", "acarbose",
    "miglitol", "troglitazone", "tolazamide", "insulin",
    "glyburide-metformin", "glipizide-metformin",
    "glimepiride-pioglitazone", "metformin-rosiglitazone",
    "metformin-pioglitazone", "change", "diabetesMed"
]


def load_raw(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, low_memory=False)
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    # Replace ? with NaN then drop rows with too many missing values
    df = df.replace("?", pd.NA)

    # Drop high-missing and irrelevant columns
    df = df.drop(columns=[c for c in COLS_TO_DROP if c in df.columns])

    # Drop rows where race is missing (small number)
    df = df.dropna(subset=["race"])

    return df


def make_target(df: pd.DataFrame) -> pd.DataFrame:
    df["readmitted_binary"] = (df["readmitted"] == "<30").astype(int)
    df = df.drop(columns=["readmitted"])
    return df


def encode(df: pd.DataFrame) -> pd.DataFrame:
    cols = [c for c in CATEGORICAL_COLS if c in df.columns]
    df[cols] = df[cols].astype(str)
    df = pd.get_dummies(df, columns=cols, drop_first=True)
    return df


def split(df: pd.DataFrame, test_size: float = 0.2, seed: int = 42):
    X = df.drop(columns=["readmitted_binary"])
    y = df["readmitted_binary"]
    return train_test_split(X, y, test_size=test_size, random_state=seed, stratify=y)


def run_pipeline(raw_path: str):
    df = load_raw(raw_path)
    print(f"Loaded: {df.shape}")

    df = clean(df)
    print(f"After cleaning: {df.shape}")

    df = make_target(df)
    print(f"Target distribution:\n{df['readmitted_binary'].value_counts()}")

    df = encode(df)
    print(f"After encoding: {df.shape}")

    X_train, X_test, y_train, y_test = split(df)
    print(f"Train: {X_train.shape}, Test: {X_test.shape}")

    return X_train, X_test, y_train, y_test
