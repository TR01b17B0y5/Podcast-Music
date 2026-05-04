import pandas as pd
import os

def load_data():
    base_path = os.getenv("DATA_PATH", "/kaggle/input/playground-series-s5e4")

    train = pd.read_csv(f"{base_path}/train.csv")
    test = pd.read_csv(f"{base_path}/test.csv")

    return train, test
