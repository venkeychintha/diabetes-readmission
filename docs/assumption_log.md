# Assumption Log

## Dataset Assumptions

1. **Binary target definition**
   The original `readmitted` column has 3 values: `<30`, `>30`, `NO`.
   We map `<30` → 1 (positive) and everything else → 0 (negative).
   Assumption: only readmission within 30 days is clinically relevant.

2. **Missing values marked as `?`**
   The dataset uses `?` to represent missing values.
   We replace all `?` with `NaN` and drop rows where `race` is missing.
   Assumption: rows with missing race are too few to impute reliably.

3. **Dropped columns**
   The following columns were dropped:
   - `encounter_id`, `patient_nbr` — identifiers, not predictive
   - `weight`, `payer_code`, `medical_specialty` — >40% missing
   - `examide`, `citoglipton` — only one unique value, no signal
   - `diag_1`, `diag_2`, `diag_3` — thousands of ICD codes create
     too many sparse features, hurting model performance

4. **Diagnosis codes excluded**
   ICD diagnosis codes were excluded because one-hot encoding them
   creates 2000+ sparse features. With more time, these could be
   grouped by disease category (first digit of ICD code).

## Model Assumptions

5. **Class imbalance handled via class weights**
   The dataset is imbalanced (~88% negative, ~12% positive).
   We use `class_weight="balanced"` rather than oversampling (SMOTE)
   to keep the pipeline simple and reproducible.

6. **Feature encoding at inference time**
   Categorical features are one-hot encoded at inference time and
   aligned to training features using `reindex`. Unseen categories
   default to 0.

7. **No feature selection applied**
   All available features after dropping excluded columns are used.
   With more time, feature importance analysis would guide selection.

## Infrastructure Assumptions

8. **CPU-only deployment**
   The model and service are designed for CPU inference only.
   No GPU acceleration is needed for Logistic Regression.

9. **Single model version loaded at startup**
   The API loads the latest model artifact at startup.
   Hot-reloading of models is not supported in this version.

10. **Local artifact storage**
    Model artifacts are stored on the local filesystem.
    In production, these would be stored in object storage (S3, GCS).
