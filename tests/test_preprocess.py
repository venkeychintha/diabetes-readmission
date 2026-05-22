import pandas as pd
import pytest
from src.data.preprocess import clean, make_target, encode, split


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "race": ["Caucasian", "?", "AfricanAmerican"],
        "gender": ["Male", "Female", "Male"],
        "age": ["[70-80)", "[50-60)", "[40-50)"],
        "admission_type_id": [1, 2, 3],
        "discharge_disposition_id": [1, 2, 3],
        "admission_source_id": [7, 1, 2],
        "time_in_hospital": [3, 5, 2],
        "num_lab_procedures": [40, 50, 30],
        "num_procedures": [1, 2, 0],
        "num_medications": [15, 20, 10],
        "number_outpatient": [0, 1, 0],
        "number_emergency": [0, 0, 1],
        "number_inpatient": [0, 1, 0],
        "number_diagnoses": [9, 7, 5],
        "max_glu_serum": ["None", ">300", "None"],
        "A1Cresult": ["None", ">8", "None"],
        "metformin": ["No", "Yes", "No"],
        "repaglinide": ["No", "No", "No"],
        "nateglinide": ["No", "No", "No"],
        "chlorpropamide": ["No", "No", "No"],
        "glimepiride": ["No", "No", "No"],
        "acetohexamide": ["No", "No", "No"],
        "glipizide": ["No", "No", "No"],
        "glyburide": ["No", "No", "No"],
        "tolbutamide": ["No", "No", "No"],
        "pioglitazone": ["No", "No", "No"],
        "rosiglitazone": ["No", "No", "No"],
        "acarbose": ["No", "No", "No"],
        "miglitol": ["No", "No", "No"],
        "troglitazone": ["No", "No", "No"],
        "tolazamide": ["No", "No", "No"],
        "insulin": ["No", "Up", "No"],
        "change": ["No", "Ch", "No"],
        "diabetesMed": ["Yes", "Yes", "No"],
        "glyburide-metformin": ["No", "No", "No"],
        "glipizide-metformin": ["No", "No", "No"],
        "glimepiride-pioglitazone": ["No", "No", "No"],
        "metformin-rosiglitazone": ["No", "No", "No"],
        "metformin-pioglitazone": ["No", "No", "No"],
        "readmitted": ["<30", ">30", "NO"],
    })


def test_clean_removes_missing_race(sample_df):
    result = clean(sample_df)
    assert result.shape[0] == 2


def test_make_target_binary(sample_df):
    df = clean(sample_df)
    df = make_target(df)
    assert "readmitted_binary" in df.columns
    assert set(df["readmitted_binary"].unique()).issubset({0, 1})


def test_encode_returns_dummies(sample_df):
    df = clean(sample_df)
    df = make_target(df)
    df = encode(df)
    assert df.select_dtypes(include="object").shape[1] == 0


def test_split_sizes(sample_df):
    df = clean(sample_df)
    df = make_target(df)
    df = encode(df)
    X = df.drop(columns=["readmitted_binary"])
    y = df["readmitted_binary"]
    assert len(X) == len(y)
    assert len(X) > 0

