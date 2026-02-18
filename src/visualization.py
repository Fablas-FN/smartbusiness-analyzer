import matplotlib.pyplot as plt
import pandas as pd

def plot_monthly_revenue(df, save_path="../reports/charts/monthly_revenue.png"):
    """
    Gruppiert Umsatz nach Monat und erstellt Balkendiagramm.
    """
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")
    monthly_revenue = df.groupby("month")["revenue"].sum()

    monthly_revenue.plot(kind="bar", color="skyblue")
    plt.title("Monatlicher Umsatz")
    plt.xlabel("Monat")
    plt.ylabel("Umsatz")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
