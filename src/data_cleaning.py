def clean_data(df):
    """
    Bereinigt die Daten.
    Entfernt fehlende Werte.
    """
    df = df.dropna()
    return df
