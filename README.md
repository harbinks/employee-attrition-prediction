# Employee Attrition Prediction

An end-to-end Machine Learning project focused on predicting employee attrition (whether an employee is likely to leave a company) using HR analytics data.

This project combines **data cleaning, exploratory data analysis (EDA), machine learning modeling, feature importance analysis, and Streamlit deployment** to provide business insights into employee retention.

## Live Demo

🔗 https://employee-attrition-prediction-2026.streamlit.app/

## GitHub Repository

🔗 GitHub Repo: YOUR_GITHUB_LINK_HERE

---

## Project Overview

Employee attrition is a major challenge for organizations, as losing employees can increase hiring costs, reduce productivity, and impact overall team performance.

The objective of this project is to:

- Predict whether an employee is likely to leave the company.
- Identify the major factors influencing attrition.
- Build a deployable machine learning solution for HR analytics.

This project helps HR teams identify employees at higher risk of leaving and take preventive measures.

---

## Problem Statement

Organizations often struggle to understand:

- Why employees leave
- Which employees are at risk
- What workplace factors contribute to attrition

Using machine learning, this project predicts employee attrition based on workplace, salary, and employee-related factors.

---

## Dataset Information

The dataset contains employee-related features such as:

- Age
- Monthly Income
- Distance From Home
- Overtime
- Job Satisfaction
- Work-Life Balance
- Years at Company
- Promotion History
- Job Role
- Department
- Performance Rating

### Target Variable

**Attrition**
- Yes → Employee likely to leave
- No → Employee likely to stay

---

## Project Workflow

### 1. Data Cleaning & Preprocessing

Performed:

- Missing value analysis
- Duplicate checking
- Removal of irrelevant columns
- Feature encoding
- Data preparation for machine learning

### 2. Exploratory Data Analysis (EDA)

Analyzed employee behavior and attrition patterns through visualizations.

Key observations:

- Employees working overtime showed significantly higher attrition rates.
- Employees with poor work-life balance had a higher tendency to leave.
- Younger and newly joined employees showed higher attrition.
- Sales department employees showed relatively higher resignation trends.
- Employees with lower monthly income showed increased attrition risk.

---

## Machine Learning Models Used

### Logistic Regression
Used as the baseline model.

### Random Forest Classifier
Used to compare performance with Logistic Regression.

### Balanced Logistic Regression
Since the dataset was imbalanced, `class_weight='balanced'` was applied to improve prediction performance for employees likely to leave.

This improved the model's ability to identify attrition cases.

---

## Model Performance

### Best Model: Balanced Logistic Regression

**Classification Report:**

| Metric | Score |
|--------|------|
| Accuracy | 75% |
| Recall (Attrition) | 77% |
| F1 Score | 50% |

### Why this model?

Although accuracy slightly decreased, recall for attrition improved significantly.

In real-world HR analytics:

> Correctly identifying employees likely to leave is more important than simply achieving high accuracy.

---

## Feature Importance Insights

The most influential factors affecting employee attrition were:

1. OverTime
2. Department
3. Years Since Last Promotion
4. Number of Companies Worked
5. Years At Company
6. Marital Status
7. Distance From Home

### Key Business Insight

Employees working overtime and employees without promotions for longer periods were more likely to leave.

---

## Streamlit Deployment

A Streamlit web application was built to allow users to:

- Enter employee information
- Predict attrition risk
- Get instant results

The application uses the trained machine learning model and scaler saved using **Joblib**.

---

## Project Structure

```bash
Employee-Attrition-Prediction/
│── app/
│   └── app.py
│
│── data/
│   └── HR-Employee-Attrition.csv
│
│── models/
│   ├── employee_attrition_model.pkl
│   └── scaler.pkl
│
│── notebooks/
│   ├── data_cleaning.ipynb
│   └── EDA.ipynb
│
│── requirements.txt
│── README.md