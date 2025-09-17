# pages/AAV_Reagent_Calculator.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="AAV Reagent Calculator", layout="wide")

st.title("🧬 AAV Production Reagent Calculator")
st.markdown("Calculate reagent volumes for AAV production based on a 4:2:1 ratio of Capsid:Helper:Target Gene plasmids.")

# --- Hard-coded values from the lentivirus reference table, including culture volume ---
PLATE_DATA = {
    "6 well":    {"total_plasmid_ng": 8160, "cacl2_ul": 25.4, "dna_mix_ul": 100, "hbs_ul": 100, "culture_ul": 2000},
    "12 well":   {"total_plasmid_ng": 3260, "cacl2_ul": 10.16, "dna_mix_ul": 40,  "hbs_ul": 40,  "culture_ul": 800},
    "24 well":   {"total_plasmid_ng": 1632, "cacl2_ul": 5.08,  "dna_mix_ul": 20,  "hbs_ul": 20,  "culture_ul": 400},
    "48 well":   {"total_plasmid_ng": 816, "cacl2_ul": 2.54,  "dna_mix_ul": 10,  "hbs_ul": 10,  "culture_ul": 200},
    "96 well":   {"total_plasmid_ng": 408,  "cacl2_ul": 1.27,  "dna_mix_ul": 5,   "hbs_ul": 5,   "culture_ul": 100},
    "100mm dish":{"total_plasmid_ng": 40800,"cacl2_ul": 127,   "dna_mix_ul": 500, "hbs_ul": 500, "culture_ul": 10000},
    "150mm dish":{"total_plasmid_ng": 73440,"cacl2_ul": 229,   "dna_mix_ul": 900, "hbs_ul": 900, "culture_ul": 20000}
}

# --- Main Page Inputs ---
st.header("1. Setup")
col1, col2 = st.columns(2)
with col1:
    plate_format = st.selectbox(
        "Select Plate Format:",
        options=list(PLATE_DATA.keys())
    )
with col2:
    num_wells = st.number_input(
        "Number of Wells/Plates:",
        min_value=1,
        value=1,
        step=1
    )

st.header("2. Input Plasmid Concentrations (ng/μL)")
col1, col2, col3 = st.columns(3)
with col1:
    target_gene_conc = st.number_input("Target Gene", min_value=0.1)
with col2:
    helper_conc = st.number_input("Helper", min_value=0.1)
with col3:
    capsid_conc = st.number_input("Capsid", min_value=0.1)


# --- Calculation Logic & Display ---
if st.button("Calculate Volumes", type="primary"):
    RATIO_SUM = 7
    params = PLATE_DATA[plate_format]
    total_plasmid_mass_per_well = params["total_plasmid_ng"]

    target_gene_mass = total_plasmid_mass_per_well / RATIO_SUM
    helper_mass = 2 * target_gene_mass
    capsid_mass = 4 * target_gene_mass

    try:
        target_gene_vol = target_gene_mass / target_gene_conc
        helper_vol = helper_mass / helper_conc
        capsid_vol = capsid_mass / capsid_conc
    except ZeroDivisionError:
        st.error("Plasmid concentration cannot be zero.")
        st.stop()

    total_plasmid_vol = target_gene_vol + helper_vol + capsid_vol
    cacl2_vol_per_well = params["cacl2_ul"]
    dna_mix_vol = params["dna_mix_ul"]
    dw_vol = dna_mix_vol - total_plasmid_vol - cacl2_vol_per_well

    # --- Display Results ---
    st.header("3. Master Mix Recipe")
    st.info(f"Calculations for **{num_wells}** well(s) of a **{plate_format}** plate.")

    final_total_volume = params["culture_ul"] + params["hbs_ul"] + dna_mix_vol
    total_vol_col_name = f"Total Volume for {num_wells} Well(s) (μL)"
    
    results_data = {
        "Component": ["Target Gene (pAAV)", "Helper", "Capsid", "2M CaCl₂", "Water (DW)", "2X HBS", "Culture Volume (ul)", "Final total volume for well (ul)"],
        "Volume per Well (μL)": [target_gene_vol, helper_vol, capsid_vol, cacl2_vol_per_well, dw_vol, params["hbs_ul"], params["culture_ul"], final_total_volume],
        f"Total Volume for {num_wells} Well(s) (μL)": [
            target_gene_vol * num_wells,
            helper_vol * num_wells,
            capsid_vol * num_wells,
            cacl2_vol_per_well * num_wells,
            dw_vol * num_wells,
            params["hbs_ul"] * num_wells,
            params["culture_ul"] * num_wells,
            final_total_volume * num_wells
        ]
    }
    results_df = pd.DataFrame(results_data)

    st.dataframe(
        results_df.style.format({
            "Volume per Well (μL)": "{:.1f}",
            total_vol_col_name: "{:.1f}"
        }).hide(axis="index"),
        use_container_width=True
    )

    if dw_vol < 0:
        st.warning(
            "⚠️ **Warning: Negative Water Volume**\n\n"
            f"The calculated volume for water is **{dw_vol:.1f} μL**. This means the total volume of your plasmids is too high for the transfection mix. Please increase the concentration of your plasmids."
        )
