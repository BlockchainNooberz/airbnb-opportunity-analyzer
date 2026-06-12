"""
Airbnb Mega Opportunities Analyzer
High-yield market identification and ROI modeling for short-term rentals
Author: Andrew Elston | github.com/BlockchainNooberz
"""
import pandas as pd
import numpy as np
from datetime import datetime
from typing import List, Dict

class AirbnbAnalyzer:
    def __init__(self):
        self.markets = []

    def get_high_yield_markets(self) -> List[Dict]:
        return [
            {"city": "Miami, FL", "adr": 180, "occupancy": 0.75, "annual_rev": 49275, "reg_risk": "Low", "growth": "Very High"},
            {"city": "Nashville, TN", "adr": 155, "occupancy": 0.78, "annual_rev": 41975, "reg_risk": "Low", "growth": "High"},
            {"city": "Lisbon, Portugal", "adr": 110, "occupancy": 0.82, "annual_rev": 32934, "reg_risk": "Medium", "growth": "High"},
            {"city": "Barcelona, Spain", "adr": 120, "occupancy": 0.80, "annual_rev": 35040, "reg_risk": "Medium", "growth": "High"},
            {"city": "Austin, TX", "adr": 165, "occupancy": 0.72, "annual_rev": 43362, "reg_risk": "Low", "growth": "Very High"},
        ]

    def calculate_roi(self, annual_rev: float, property_cost: float, operating_expense_ratio: float = 0.35) -> float:
        net_income = annual_rev * (1 - operating_expense_ratio)
        return (net_income / property_cost) * 100

    def generate_report(self):
        markets = self.get_high_yield_markets()
        df = pd.DataFrame(markets)
        df["estimated_roi_pct"] = df["annual_rev"].apply(lambda r: round(self.calculate_roi(r, 350000), 1))
        print("\n" + "="*65)
        print("AIRBNB MARKET OPPORTUNITY REPORT")
        print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("="*65)
        print(df[["city","annual_rev","occupancy","estimated_roi_pct","reg_risk"]].to_string(index=False))

if __name__ == "__main__":
    AirbnbAnalyzer().generate_report()
