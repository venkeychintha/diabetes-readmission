from ucimlrepo import fetch_ucirepo
import pandas as pd
import os

print("Downloading dataset...")

dataset = fetch_ucirepo(id=296)

df = dataset.data.features
df["readmitted"] = dataset.data.targets

os.makedirs("data/raw", exist_ok=True)
df.to_csv("data/raw/diabetic_data.csv", index=False)

print(f"Done! Shape: {df.shape}")
print(f"Saved to data/raw/diabetic_data.csv")
