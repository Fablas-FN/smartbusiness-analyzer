def save_monthly_report(df, path="../reports/monthly_reports/monthly_report.csv"):
    """
    Speichert die berechneten KPIs als CSV-Datei.
    """
    df.to_csv(path, index=False)
    print(f"Report gespeichert: {path}")
