from src.data.preprocess import run_pipeline

X_train, X_test, y_train, y_test = run_pipeline("data/raw/diabetic_data.csv")
print("Preprocessing complete!")
