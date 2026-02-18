import pandas as pd

def load_sales_data(path="../data/raw/sales_data.csv"):
    """
    Liest die Rohdaten ein und gibt einen DataFrame zurück.
    """
    df = pd.read_csv(path)
    return df
