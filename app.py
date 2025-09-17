# app.py
import streamlit as st

st.set_page_config(
    page_title="In-Lab Calculator",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Welcome to the In-Lab Calculator!")
st.sidebar.success("Select a calculator above.")

st.markdown(
    """
    This is an interactive web app designed to host various calculators for common lab tasks.

    **👈 Select a calculator from the sidebar** to get started!

    ### Want to add a new calculator?
    - Create a new Python file in the `pages/` directory.
    - The filename will be used as the page title (e.g., `3_My_New_Calculator.py`).
    - Write your Streamlit code in the new file!
    """
)
