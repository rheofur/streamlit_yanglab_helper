# app.py
import streamlit as st

st.set_page_config(
    page_title="In-Lab Calculator",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Main Page")
st.sidebar.success("Select a calculator above.")

st.markdown(
    """
    This is an interactive web app designed to host various calculators for common lab tasks.

    **👈 Select a calculator from the sidebar** to get started!
    """
)
