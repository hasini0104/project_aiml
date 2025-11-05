
import json
import datetime

class SustainabilityTracker:
    def __init__(self, user_name):
        self.user_name = user_name
        self.data = {}
        self.footprint_score = 0
        self.recommendations = []
        self.date = datetime.date.today()

    def collect_data(self):
        print(f"\nWelcome {self.user_name}! Let's calculate your sustainability impact.")
        self.data['electricity_usage'] = float(input("Enter monthly electricity use (kWh): "))
        self.data['water_usage'] = float(input("Enter monthly water use (liters): "))
        self.data['waste_generated'] = float(input("Enter monthly waste generated (kg): "))
        self.data['transport_km'] = float(input("Enter monthly transport distance (km): "))
        self.data['diet_type'] = input("Enter diet type (veg/non-veg/mixed): ").lower()

    def calculate_impact(self):
        carbon_from_electricity = self.data['electricity_usage'] * 0.85
        carbon_from_water = self.data['water_usage'] * 0.0003
        carbon_from_waste = self.data['waste_generated'] * 2.5
        carbon_from_transport = self.data['transport_km'] * 0.21

        if self.data['diet_type'] == 'veg':
            carbon_from_diet = 150
        elif self.data['diet_type'] == 'mixed':
            carbon_from_diet = 250
        else:
            carbon_from_diet = 400

        self.footprint_score = (
            carbon_from_electricity + carbon_from_water +
            carbon_from_waste + carbon_from_transport +
            carbon_from_diet
        )

    def generate_recommendations(self):
        if self.data['electricity_usage'] > 300:
            self.recommendations.append("Switch to LED bulbs and unplug idle devices.")
        if self.data['water_usage'] > 5000:
            self.recommendations.append("Try water-saving taps and shorter showers.")
        if self.data['transport_km'] > 400:
            self.recommendations.append("Consider public transport or carpooling.")
        if self.data['diet_type'] == 'non-veg':
            self.recommendations.append("Try plant-based meals 2–3 times a week.")

        if not self.recommendations:
            self.recommendations.append("Great job! You're already eco-conscious.")

    def show_report(self):
        print("\n========== PERSONAL SUSTAINABILITY REPORT ==========")
        print(f"User: {self.user_name}")
        print(f"Date: {self.date}")
        print(f"Total Carbon Footprint: {self.footprint_score:.2f} kg CO2e/month")
        print("\nPersonalized Recommendations:")
        for i, rec in enumerate(self.recommendations, 1):
            print(f" {i}. {rec}")
        print("====================================================")

    def save_report(self):
        report = {
            "user": self.user_name,
            "date": str(self.date),
            "data": self.data,
            "footprint_score": self.footprint_score,
            "recommendations": self.recommendations
        }
        with open(f"{self.user_name}_sustainability_report.json", "w") as f:
            json.dump(report, f, indent=4)
        print(f"\nReport saved as {self.user_name}_sustainability_report.json")


if __name__ == "__main__":
    name = input("Enter your name: ")
    tracker = SustainabilityTracker(name)
    tracker.collect_data()
    tracker.calculate_impact()
    tracker.generate_recommendations()
    tracker.show_report()
    tracker.save_report()
