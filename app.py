import streamlit as st
import numpy as np
import pandas as pd
import pickle

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(page_title="Insurance Charges Prediction", layout="wide")

st.title("🏥 Insurance Charges Prediction System")
st.write("Predict insurance charges based on medical and demographic details.")

# -----------------------------------
# LOAD FINAL MODEL
# -----------------------------------
model = pickle.load(open("insurance_model_final.pkl", "rb"))
feature_order = pickle.load(open("feature_order_final.pkl", "rb"))

# -----------------------------------
# USER INPUT SECTION
# -----------------------------------
st.header("Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 100, 30)
    sex = st.selectbox("Sex", ["male", "female"])
    bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
    children = st.number_input("Number of Children", 0, 10, 0)
    smoker = st.selectbox("Smoker", ["yes", "no"])

with col2:
    claim_amount = st.number_input(
        "Claim Amount",
        min_value=0.0,
        max_value=200000.0,
        value=1000.0
    )

    past_consultations = st.number_input(
        "Past Consultations",
        min_value=0,
        max_value=50,
        value=5
    )

    hospital_exp = st.number_input(
        "Hospital Expenditure",
        min_value=0.0,
        max_value=300000000.0,
        value=1000.0
    )

    past_hosp = st.number_input(
        "Past Hospitalizations",
        min_value=0,
        max_value=20,
        value=0
    )

    salary = st.number_input(
        "Annual Salary",
        min_value=0.0,
        max_value=5000000000.0,
        value=5000000.0
    )

    region = st.selectbox(
        "Region",
        ["southeast", "southwest", "northwest", "northeast"]
    )

# -----------------------------------
# ENCODE INPUTS
# -----------------------------------
sex = 0 if sex == "male" else 1
smoker = 1 if smoker == "yes" else 0

region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0

# -----------------------------------
# CREATE INPUT DATAFRAME
# -----------------------------------
input_dict = {
    "age": age,
    "sex": sex,
    "bmi": bmi,
    "children": children,
    "smoker": smoker,
    "Claim_Amount": claim_amount,
    "past_consultations": past_consultations,
    "Hospital_expenditure": hospital_exp,
    "NUmber_of_past_hospitalizations": past_hosp,
    "Anual_Salary": salary,
    "region_northwest": region_northwest,
    "region_southeast": region_southeast,
    "region_southwest": region_southwest
}

input_df = pd.DataFrame([input_dict])
input_df = input_df.reindex(columns=feature_order)

# -----------------------------------
# PREDICTION
# -----------------------------------
if st.button("Predict Insurance Charges"):

    prediction = model.predict(input_df)[0]

    st.success(f"Estimated Insurance Charges: ${prediction:,.2f}")

    # Risk Category
    if prediction < 8000:
        st.info("🟢 Low Insurance Risk")
    elif prediction < 20000:
        st.warning("🟡 Moderate Insurance Risk")
    else:
        st.error("🔴 High Insurance Risk")