from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]

def load_iris_data() -> pd.DataFrame:
    """
    load the iris dataset from the data folder 
    and then return a DataFrame
    """
    data_path= PROJECT_ROOT / 'data'/'iris.csv'
    df= pd.read_csv(data_path)
    return df
