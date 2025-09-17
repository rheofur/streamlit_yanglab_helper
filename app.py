# app.py
import streamlit as st

st.set_page_config(
    page_title="In-Lab Calculator",
    page_icon="🔬",
    layout="wide"
)

# This CSS hides the page link for this file ("app.py") in the sidebar.
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] ul > li:first-child {
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

# The title here only affects the content on the page, not the sidebar.
st.title("🔬 Welcome to the In-Lab Calculator!")
st.sidebar.success("Select a calculator above.")

st.markdown(
    """
    This is an interactive web app designed to host various calculators for common lab tasks.

    **👈 Select a calculator from the sidebar** to get started!
    """
)
