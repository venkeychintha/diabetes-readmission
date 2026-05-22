import argparse
from src.models.train import train

parser = argparse.ArgumentParser()
parser.add_argument("--data", default="data/raw/diabetic_data.csv")
parser.add_argument("--artifacts", default="artifacts")
args = parser.parse_args()

train(data_path=args.data, artifact_dir=args.artifacts)
