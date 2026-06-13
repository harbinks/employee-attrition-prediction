import streamlit as st
import joblib
import numpy as np
from pathlib import Path

# -----------------------------
# Load model and scaler
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(
    BASE_DIR / "models" / "employee_attrition_model.pkl"
)

scaler = joblib.load(
    BASE_DIR / "models" / "scaler.pkl"
)

# -----------------------------
# Streamlit UI
# -----------------------------

st.title("Employee Attrition Prediction")

st.write(
    "Predict whether an employee is likely to leave the company."
)

# User Inputs
age = st.slider(
    "Age",
    18,
    60,
    30
)

distance = st.slider(
    "Distance From Home",
    1,
    30,
    10
)

income = st.number_input(
    "Monthly Income",
    min_value=1000,
    max_value=50000,
    value=5000
)

years_company = st.slider(
    "Years At Company",
    0,
    40,
    5
)

overtime = st.selectbox(
    "OverTime",
    ["No", "Yes"]
)

# Convert categorical input
overtime = 1 if overtime == "Yes" else 0

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Attrition"):

    # Realistic average employee values
    input_data = np.array([[
        age,           # Age
        1,             # BusinessTravel
        800,           # DailyRate
        1,             # Department
        distance,      # DistanceFromHome
        3,             # Education
        1,             # EducationField
        3,             # EnvironmentSatisfaction
        1,             # Gender
        65,            # HourlyRate
        3,             # JobInvolvement
        2,             # JobLevel
        4,             # JobRole
        3,             # JobSatisfaction
        1,             # MaritalStatus
        income,        # MonthlyIncome
        14000,         # MonthlyRate
        2,             # NumCompaniesWorked
        overtime,      # OverTime
        15,            # PercentSalaryHike
        3,             # PerformanceRating
        3,             # RelationshipSatisfaction
        1,             # StockOptionLevel
        10,            # TotalWorkingYears
        2,             # TrainingTimesLastYear
        3,             # WorkLifeBalance
        years_company, # YearsAtCompany
        4,             # YearsInCurrentRole
        1,             # YearsSinceLastPromotion
        4              # YearsWithCurrManager
    ]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)

    # Show Result
    if prediction[0] == 1:
        st.error(
            "⚠️ Employee is likely to leave the company."
        )
    else:
        st.success(
            "✅ Employee is likely to stay."
        )