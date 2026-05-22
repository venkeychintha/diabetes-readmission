from pydantic import BaseModel, Field
from typing import Optional


class PatientRecord(BaseModel):
    race: Optional[str] = "Caucasian"
    gender: str = "Male"
    age: str = "[70-80)"
    admission_type_id: int = 1
    discharge_disposition_id: int = 1
    admission_source_id: int = 7
    time_in_hospital: int = 3
    num_lab_procedures: int = 40
    num_procedures: int = 1
    num_medications: int = 15
    number_outpatient: int = 0
    number_emergency: int = 0
    number_inpatient: int = 0
    number_diagnoses: int = 9
    max_glu_serum: Optional[str] = "None"
    A1Cresult: Optional[str] = "None"
    metformin: str = "No"
    repaglinide: str = "No"
    nateglinide: str = "No"
    chlorpropamide: str = "No"
    glimepiride: str = "No"
    acetohexamide: str = "No"
    glipizide: str = "No"
    glyburide: str = "No"
    tolbutamide: str = "No"
    pioglitazone: str = "No"
    rosiglitazone: str = "No"
    acarbose: str = "No"
    miglitol: str = "No"
    troglitazone: str = "No"
    tolazamide: str = "No"
    insulin: str = "No"
    change: str = "No"
    diabetesMed: str = "Yes"
    glyburide_metformin: str = "No"
    glipizide_metformin: str = "No"
    glimepiride_pioglitazone: str = "No"
    metformin_rosiglitazone: str = "No"
    metformin_pioglitazone: str = "No"


class PredictionResponse(BaseModel):
    model_config = {"protected_namespaces": ()}

    readmitted_within_30_days: bool
    probability: float = Field(..., ge=0.0, le=1.0)
    model_version: str

