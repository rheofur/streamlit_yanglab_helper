# pages/Mouse_Age_Calculator.py
import streamlit as st
from datetime import date, timedelta

# --- Page Configuration ---
st.set_page_config(page_title="Mouse Age Calculator", layout="wide")
st.title("🐁 Mouse Age Calculator")
st.markdown("Use the tools below to calculate a mouse's age or its date of birth.")

# --- SEPARATOR ---
st.markdown("---")

# --- Calculator 1: Calculate Age from Date of Birth ---
st.header("1. Calculate Age from Date of Birth")

# Input for DOB
dob = st.date_input("Select Mouse Date of Birth:", max_value=date.today(), key="dob_input")

# --- Calculation Logic (runs automatically on input change) ---
if dob:
    today = date.today()
    age_delta = today - dob
    age_in_days = age_delta.days
    age_in_weeks = age_in_days / 7

    st.success("### Results")
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Age in Days", value=f"{age_in_days} days")

    with col2:
        st.metric(label="Age in Weeks", value=f"{age_in_weeks:.2f} weeks")

# --- SEPARATOR ---
st.markdown("---")

# --- Calculator 2: Calculate Date of Birth from Age ---
st.header("2. Calculate Date of Birth from Age")

# Inputs for Age Range
col1, col2 = st.columns(2)
with col1:
    age_unit = st.radio("Select Age Unit:", ("Weeks", "Days"), horizontal=True, key="age_unit_radio")

with col2:
    if age_unit == "Weeks":
        desired_age_min = st.number_input("Minimum Age (weeks):", min_value=0.0, step=0.1, format="%.1f")
        desired_age_max = st.number_input("Maximum Age (weeks):", min_value=desired_age_min, step=0.1, format="%.1f")
    else: # Days
        desired_age_min = st.number_input("Minimum Age (days):", min_value=0, step=1)
        desired_age_max = st.number_input("Maximum Age (days):", min_value=desired_age_min, step=1)

# --- Calculation Logic (runs on button press) ---
if st.button("Calculate Birth Date Range"):
    today = date.today()

    # Convert age range to days
    if age_unit == "Weeks":
        min_days = int(desired_age_min * 7)
        max_days = int(desired_age_max * 7)
    else: # Days
        min_days = desired_age_min
        max_days = desired_age_max

    # Calculate the date range
    latest_dob = today - timedelta(days=min_days)
    earliest_dob = today - timedelta(days=max_days)

    st.success("### Results")
    st.markdown(f"To have a mouse between **{desired_age_min} and {desired_age_max} {age_unit.lower()} old** today, its date of birth must be between:")

    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.metric("Earliest Date of Birth", earliest_dob.strftime('%B %d, %Y'))
    with res_col2:
        st.metric("Latest Date of Birth", latest_dob.strftime('%B %d, %Y'))
