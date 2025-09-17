# pages/Mouse_Age_Calculator.py
import streamlit as st
from datetime import date, timedelta

st.set_page_config(page_title="Mouse Age Calculator", layout="wide")
st.title("🐁 Mouse Age Calculator")

# --- DATE SELECTION FOR ALL CALCULATIONS ---
st.markdown("---")
current_date = st.date_input("Select 'current day' for calculations:", value=date.today())
st.markdown("---")


# --- Calculator 1: Calculate Age from Date of Birth ---
st.header("1. Calculate Age from Date of Birth")
dob = st.date_input("Select Mouse Date of Birth:", max_value=current_date, key="dob_input")

if dob:
    age_delta = current_date - dob
    age_in_days = age_delta.days
    age_in_weeks = age_in_days / 7.0

    st.success("### Results")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Age in Days", value=f"{age_in_days} days")
    with col2:
        st.metric(label="Age in Weeks", value=f"{age_in_weeks:.1f} weeks")

st.markdown("---")


# --- Calculator 2: Calculate Date of Birth from Age ---
st.header("2. Calculate Date of Birth from Age")
col1, col2 = st.columns(2)

with col1:
    age_unit = st.radio("Select Age Unit:", ("Weeks", "Days"), horizontal=True)

with col2:
    if age_unit == "Weeks":
        # Input for weeks is now an integer
        desired_age_min = st.number_input("Minimum Age (weeks):", min_value=0, step=1)
        desired_age_max = st.number_input("Maximum Age (weeks):", min_value=desired_age_min, step=1)
    else: # Days
        desired_age_min = st.number_input("Minimum Age (days):", min_value=0, step=1)
        desired_age_max = st.number_input("Maximum Age (days):", min_value=desired_age_min, step=1)

if st.button("Calculate Birth Date Range"):
    if age_unit == "Weeks":
        # Correctly calculate the range for weeks
        min_days = desired_age_min * 7
        max_days = (desired_age_max * 7) + 6 # Add 6 days to complete the week
    else: # Days
        min_days = desired_age_min
        max_days = desired_age_max

    latest_dob = current_date - timedelta(days=min_days)
    earliest_dob = current_date - timedelta(days=max_days)

    st.success("### Results")
    st.markdown(f"To have a mouse between **{desired_age_min} and {desired_age_max} {age_unit.lower()} old** on **{current_date.strftime('%Y-%m-%d')}**, its date of birth must be between:")

    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.metric("Earliest Date of Birth", earliest_dob.strftime('%B %d, %Y'))
    with res_col2:
        st.metric("Latest Date of Birth", latest_dob.strftime('%B %d, %Y'))
