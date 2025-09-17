# pages/2_🐁_Mouse_Age_Calculator.py
import streamlit as st
from datetime import date, timedelta

st.set_page_config(page_title="Mouse Age Calculator", layout="wide")

st.title("🐁 Mouse Age Calculator")
st.markdown("Calculate the current age of a mouse from its date of birth.")

st.sidebar.header("Age Calculator")

# --- Calculator Inputs ---
dob = st.date_input("Select Mouse Date of Birth:", max_value=date.today())

# --- Calculation Logic ---
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

    # --- Age-related information table (Hard-coded example) ---
    st.markdown("---")
    st.subheader("Developmental Milestones (Example)")

    if age_in_days <= 14:
        stage = "Pups (pre-weaning)"
        info = "Eyes and ears are closed. Dependent on mother."
    elif 14 < age_in_days <= 28:
        stage = "Weanlings"
        info = "Begin to eat solid food. Typically weaned around 21 days."
    elif 28 < age_in_days <= 60:
        stage = "Juveniles / Young Adults"
        info = "Reach sexual maturity."
    else:
        stage = "Adults"
        info = "Considered fully grown."

    st.info(f"**Stage:** {stage}\n\n**Notes:** {info}")