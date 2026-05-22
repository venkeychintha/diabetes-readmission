import pytest
from api.predictor import load_model, predict


def test_load_model():
    model, features, version = load_model()
    assert model is not None
    assert len(features) > 0
    assert version.startswith("v_")


def test_predict_returns_valid_output():
    model, features, version = load_model()
    record = {
        "race": "Caucasian",
        "gender": "Male",
        "age": "[70-80)",
        "admission_type_id": 1,
        "discharge_disposition_id": 1,
        "admission_source_id": 7,
        "time_in_hospital": 3,
        "num_lab_procedures": 40,
        "num_procedures": 1,
        "num_medications": 15,
        "number_outpatient": 0,
        "number_emergency": 0,
        "number_inpatient": 0,
        "number_diagnoses": 9,
        "max_glu_serum": "None",
        "A1Cresult": "None",
        "metformin": "No",
        "repaglinide": "No",
        "nateglinide": "No",
        "chlorpropamide": "No",
        "glimepiride": "No",
        "acetohexamide": "No",
        "glipizide": "No",
        "glyburide": "No",
        "tolbutamide": "No",
        "pioglitazone": "No",
        "rosiglitazone": "No",
        "acarbose": "No",
        "miglitol": "No",
        "troglitazone": "No",
        "tolazamide": "No",
        "insulin": "No",
        "change": "No",
        "diabetesMed": "Yes",
        "glyburide_metformin": "No",
        "glipizide_metformin": "No",
        "glimepiride_pioglitazone": "No",
        "metformin_rosiglitazone": "No",
        "metformin_pioglitazone": "No",
    }
    prob, label = predict(record, model, features)
    assert 0.0 <= prob <= 1.0
    assert isinstance(label, bool)


def test_predict_missing_fields_handled():
    model, features, version = load_model()
    record = {"race": "Caucasian", "gender": "Male"}
    prob, label = predict(record, model, features)
    assert 0.0 <= prob <= 1.0
