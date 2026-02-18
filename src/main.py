from data_loader import load_sales_data
from data_cleaning import clean_data
from kpi_calculator import calculate_kpis
from visualization import plot_monthly_revenue
from report_generator import save_monthly_report
from forecast import forecast_revenue

def main():
    # 1️⃣ Daten laden
    df = load_sales_data()
    
    # 2️⃣ Daten bereinigen
    df = clean_data(df)
    
    # 3️⃣ KPIs berechnen
    df, total_revenue, total_profit = calculate_kpis(df)
    print("Gesamtumsatz:", total_revenue)
    print("Gesamtgewinn:", total_profit)
    
    # 4️⃣ Monatsumsatz visualisieren
    plot_monthly_revenue(df)
    
    # 5️⃣ Report speichern
    save_monthly_report(df)
    
    # 6️⃣ Forecast (Platzhalter)
    forecast_revenue(df)

if __name__ == "__main__":
    main()
