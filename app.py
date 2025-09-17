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
