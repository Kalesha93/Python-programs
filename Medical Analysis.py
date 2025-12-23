import pandas as pd

# Sample dataset (can be CSV in real case)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 45, 35, 50, 60],
    "BloodPressure": [120, 145, 135, 155, 160],
    "Cholesterol": [180, 220, 200, 250, 260],
    "BloodSugar": [90, 150, 110, 160, 170]
}

df = pd.DataFrame(data)

# Function to categorize risk
def calculate_risk(row):
    if row["BloodPressure"] > 150 or row["Cholesterol"] > 240 or row["BloodSugar"] > 160:
        return "High Risk"
    elif row["BloodPressure"] > 130 or row["Cholesterol"] > 220 or row["BloodSugar"] > 140:
        return "Moderate Risk"
    else:
        return "Low Risk"

# Apply risk calculation
df["RiskLevel"] = df.apply(calculate_risk, axis=1)

# Basic statistics
avg_age = df["Age"].mean()
avg_bp = df["BloodPressure"].mean()
avg_chol = df["Cholesterol"].mean()
avg_sugar = df["BloodSugar"].mean()

# Display results
print("Patient Data with Risk Levels:\n")
print(df)
print("\nAverage Statistics:")
print(f"Age: {avg_age:.1f}, Blood Pressure: {avg_bp:.1f}, Cholesterol: {avg_chol:.1f}, Blood Sugar: {avg_sugar:.1f}")

# Count of risk categories
print("\nRisk Category Counts:")
print(df["RiskLevel"].value_counts())
