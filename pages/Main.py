import streamlit as st

# The title here only affects the content on the page, not the sidebar.
st.title("🔬 Welcome to the In-Lab Calculator!")
st.sidebar.success("Select a calculator above.")

st.markdown(
    """
    This is an interactive web app designed to host various calculators for common lab tasks.

    **👈 Select a calculator from the sidebar** to get started!
    """
)
