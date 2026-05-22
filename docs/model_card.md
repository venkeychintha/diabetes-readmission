# Model Card — Diabetes 30-Day Readmission Predictor

## Model Details
- **Model type:** Logistic Regression with StandardScaler pipeline
- **Framework:** scikit-learn
- **Version:** v_20260521_183933
- **Task:** Binary classification (readmitted within 30 days: yes/no)
- **Input:** 126 patient features (demographic, clinical, medication)
- **Output:** Probability score (0–1) and binary label

## Intended Use
- **Primary use:** Assist clinical teams in identifying diabetic patients
  at high risk of 30-day hospital readmission
- **Intended users:** Healthcare data teams, clinical decision support systems
- **Out-of-scope uses:** Not for autonomous clinical decision-making.
  Must be reviewed by a qualified clinician before acting on predictions.

## Training Data
- **Dataset:** Diabetes 130-US Hospitals for Years 1999–2008 (UCI)
- **Records:** 99,493 patient encounters after cleaning
- **Period:** 1999–2008, 130 US hospitals
- **Target distribution:** 88% negative (no early readmission), 12% positive

## Performance Metrics (Test Set)
| Metric | Value |
|--------|-------|
| ROC-AUC | 0.6713 |
| F1 Score (class 1) | 0.2728 |
| Recall (class 1) | 0.54 |
| Precision (class 1) | 0.18 |
| Accuracy | 0.68 |

## Limitations
- **Class imbalance:** Dataset is heavily imbalanced (88/12 split).
  The model trades precision for recall on the positive class.
- **Temporal drift:** Trained on 1999–2008 data. Clinical practices
  and medications have changed significantly since then.
- **Missing diagnosis codes:** ICD diagnosis codes were excluded due
  to high cardinality. This removes potentially important clinical signal.
- **Demographic bias:** Performance may vary across race and age groups.
  Fairness evaluation across subgroups was not performed.
- **Not validated clinically:** This model has not been validated in
  a real clinical environment.

## Known Risks
- High false positive rate (low precision for class 1) may cause
  alert fatigue among clinical staff
- Model may underperform on patient populations underrepresented
  in the 1999–2008 training data
- Sensitive fields (race, gender, age) are included as features,
  which may introduce or amplify demographic bias

## Ethical Considerations
- Race, gender, and age are included as features. In a production
  healthcare setting, fairness audits across demographic subgroups
  should be conducted before deployment.
- Model predictions should never replace clinical judgment.

## Improvements With More Time
- Group ICD diagnosis codes by disease category for better signal
- Perform fairness evaluation across race, gender, and age subgroups
- Tune classification threshold using precision-recall curve
- Use SMOTE or cost-sensitive learning for better imbalance handling
- Validate on more recent hospital data
- Add SHAP values for prediction explainability
