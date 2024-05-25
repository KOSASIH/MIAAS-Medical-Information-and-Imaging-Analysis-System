import numpy as np
import pandas as pd


class DataLoader:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def load_csv(self) -> pd.DataFrame:
        return pd.read_csv(self.data_path)

    def load_numpy(self) -> np.ndarray:
        return np.load(self.data_path)

    def load_pandas(self) -> pd.DataFrame:
        return pd.read_pickle(self.data_path)


def load_data(data_path: str, data_type: str) -> object:
    loader = DataLoader(data_path)
    if data_type == "csv":
        return loader.load_csv()
    elif data_type == "numpy":
        return loader.load_numpy()
    elif data_type == "pandas":
        return loader.load_pandas()
    else:
        raise ValueError("Invalid data type")
