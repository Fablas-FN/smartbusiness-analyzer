# kpi_calculator.py

def calculate_kpis(df):
    """
    Berechnet für jeden Datensatz Umsatz, Kosten und Gewinn.
    Gibt den erweiterten DataFrame sowie Gesamtumsatz und Gesamtgewinn zurück.
    """
    # Umsatz = Menge * Preis
    df["revenue"] = df["quantity"] * df["price"]
    
    # Kosten = Menge * Einstandspreis
    df["total_cost"] = df["quantity"] * df["cost"]
    
    # Gewinn = Umsatz - Kosten
    df["profit"] = df["revenue"] - df["total_cost"]

    # Gesamtumsatz & Gesamtgewinn
    total_revenue = df["revenue"].sum()
    total_profit = df["profit"].sum()

    return df, total_revenue, total_profit
