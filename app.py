import streamlit as st

st.set_page_config(
    page_title="In-Lab Calculator",
    page_icon="🔬",
    layout="wide"
)

# This CSS hides the first list item in the sidebar navigation, which is the "app" page.
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] ul > li:first-child {
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

# This command automatically navigates to your desired main page on first load.
st.switch_page("pages/1_Main.py")
