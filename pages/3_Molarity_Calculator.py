# pages/3_Molarity_Calculator.py
import streamlit as st
import numpy as np

st.set_page_config(page_title="Molarity & Dilution Calculator", layout="wide")

st.title("🧪 Molarity and Dilution Calculator")

# --- Molarity Calculator ---
st.header("1. Molarity Calculator")
st.latex(r'''
\left( \frac{\text{Mass}}{\text{Molecular Weight}} \right) / \text{Volume} = \text{Molarity}
''')

# 1. Added a helping text for the user
st.info("💡 **Instructions:** Fill in any three of the four fields below and click 'Calculate' to find the value of the remaining field.")

col1, col2, col3, col4 = st.columns(4)

with col1:
    mass = st.number_input("Mass", format="%.4f", value=None, placeholder="Enter value")
    mass_unit = st.selectbox("Mass Unit", ("g", "mg", "µg", "ng"))

with col2:
    mw = st.number_input("Molecular Weight (g/mol)", format="%.4f", value=None, placeholder="Enter value")

with col3:
    volume = st.number_input("Volume", format="%.4f", value=None, placeholder="Enter value")
    volume_unit = st.selectbox("Volume Unit", ("L", "mL", "µL"))

with col4:
    molarity = st.number_input("Molarity", format="%.4f", value=None, placeholder="Enter value")
    molarity_unit = st.selectbox("Molarity Unit", ("M", "mM", "µM", "nM"))

if st.button("Calculate", type="primary"):
    inputs = {
        "Mass": mass,
        "Molecular Weight": mw,
        "Volume": volume,
        "Molarity": molarity
    }
    
    empty_fields = [key for key, val in inputs.items() if val is None]

    # Unit conversion factors to base units (g, L, M)
    mass_factors = {"g": 1, "mg": 1e-3, "µg": 1e-6, "ng": 1e-9}
    volume_factors = {"L": 1, "mL": 1e-3, "µL": 1e-6}
    molarity_factors = {"M": 1, "mM": 1e-3, "µM": 1e-6, "nM": 1e-9}

    try:
        # Convert all inputs to base units for calculation
        mass_base = mass * mass_factors[mass_unit] if mass is not None else None
        mw_base = mw if mw is not None else None
        volume_base = volume * volume_factors[volume_unit] if volume is not None else None
        molarity_base = molarity * molarity_factors[molarity_unit] if molarity is not None else None

        # 2. Handle cases where the user inputs 3 or 4 values
        if len(empty_fields) == 1:
            # --- Calculate the single missing value ---
            result = 0
            field_to_calculate = empty_fields[0]
            
            if field_to_calculate == "Molarity":
                result = (mass_base / mw_base) / volume_base
                result /= molarity_factors[molarity_unit]
                st.success(f"**Calculated Molarity:** {result:.4f} {molarity_unit}")

            elif field_to_calculate == "Mass":
                result = molarity_base * volume_base * mw_base
                result /= mass_factors[mass_unit]
                st.success(f"**Calculated Mass:** {result:.4f} {mass_unit}")

            elif field_to_calculate == "Volume":
                result = (mass_base / mw_base) / molarity_base
                result /= volume_factors[volume_unit]
                st.success(f"**Calculated Volume:** {result:.4f} {volume_unit}")
                
            elif field_to_calculate == "Molecular Weight":
                result = mass_base / (molarity_base * volume_base)
                st.success(f"**Calculated Molecular Weight:** {result:.4f} g/mol")

        elif len(empty_fields) == 0:
            # --- Validate user's input when all 4 fields are filled ---
            calculated_molarity = (mass_base / mw_base) / volume_base
            
            # Compare calculated molarity with user's input molarity (using a small tolerance)
            if np.isclose(calculated_molarity, molarity_base):
                st.success("✅ **Validation successful!** The four values you entered are consistent with the formula.")
            else:
                expected_molarity_in_unit = calculated_molarity / molarity_factors[molarity_unit]
                st.warning(
                    "⚠️ **Values are not consistent.**\n\n"
                    f"Based on the Mass, Molecular Weight, and Volume you entered, the calculated Molarity should be **{expected_molarity_in_unit:.4f} {molarity_unit}**."
                )
        
        else:
            # --- Error for any other number of inputs ---
            st.error("Please provide exactly three out of the four values.")

    except (ZeroDivisionError, TypeError):
        st.error("Invalid input. Please check your values.")


st.markdown("---")

# --- Stock Dilution Calculator ---
st.header("2. Stock Dilution Calculator")
st.latex(r'''
C_1 V_1 = C_2 V_2
''')

col1, col2, col3 = st.columns(3)

with col1:
    stock_conc = st.number_input("Stock Concentration (C1)", min_value=0.0, format="%.4f")
    stock_conc_unit = st.selectbox("Stock Concentration Unit", ("M", "mM", "µM", "nM"), key="stock_conc")

with col2:
    final_conc = st.number_input("Final Concentration (C2)", min_value=0.0, format="%.4f")
    final_conc_unit = st.selectbox("Final Concentration Unit", ("M", "mM", "µM", "nM"), key="final_conc")

with col3:
    final_vol = st.number_input("Final Volume (V2)", min_value=0.0, format="%.4f")
    final_vol_unit = st.selectbox("Final Volume Unit", ("L", "mL", "µL"), key="final_vol")


if st.button("Calculate Stock Volume", type="primary"):
    if stock_conc > 0:
        # Concentration conversion factors to M
        conc_factors = {"M": 1, "mM": 1e-3, "µM": 1e-6, "nM": 1e-9}
        
        # Convert concentrations to the same unit (M)
        stock_conc_base = stock_conc * conc_factors[stock_conc_unit]
        final_conc_base = final_conc * conc_factors[final_conc_unit]

        # V1 = (C2 * V2) / C1
        required_vol = (final_conc_base * final_vol) / stock_conc_base
        
        st.success(f"You will need **{required_vol:.4f} {final_vol_unit}** of the stock solution.")
    else:
        st.error("Stock concentration must be greater than zero.")
