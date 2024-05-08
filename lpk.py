# Jalankan aplikasi dengan perintah `streamlit run filename.py`

import streamlit as st
import math

# Fungsi untuk menghitung pH untuk asam kuat


def calculate_strong_acid_pH(concentration, a):
    H_plus = concentration * a
    pH = -math.log10(H_plus)
    return H_plus, pH

# Fungsi untuk menghitung pH untuk basa kuat


def calculate_strong_base_pH(concentration, a):
    OH_minus = concentration * a
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH

# Fungsi untuk menghitung pH untuk asam lemah


def calculate_weak_acid_pH(ka, concentration):
    H_plus = math.sqrt(ka * concentration)
    pH = -math.log10(H_plus)
    return H_plus, pH

# Fungsi untuk menghitung pH untuk basa lemah


def calculate_weak_base_pH(kb, concentration):
    OH_minus = math.sqrt(kb * concentration)
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH

# Fungsi untuk menghitung pH dari massa dan volume untuk asam kuat


def calculate_strong_acid_mass_pH(mass, volume, bm):
    H_plus = (mass / volume) * bm
    pH = -math.log10(H_plus)
    return H_plus, pH

# Fungsi untuk menghitung pH dari massa dan volume untuk basa kuat


def calculate_strong_base_mass_pH(mass, volume, bm):
    OH_minus = (mass / volume) * bm
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH


# Judul aplikasi
st.title("Penghitung pH dan Konsentrasi")

# Halaman utama untuk pilihan
options = ["Menghitung dengan konsentrasi asam",
           "Menghitung dengan konsentrasi basa",
           "Menghitung dengan Massa dan Volume asam",
           "Menghitung dengan Massa dan Volume basa"]

choice = st.sidebar.radio("Pilih Metode", options)

if choice == "Menghitung dengan Konsentrasi Asam Kuat":
    st.subheader("Menghitung pH dan [H+] dari Konsentrasi Asam Kuat")

    # Pilih senyawa asam kuat
    strong_acids = {
        "Asam Klorida (HCl)": 1,
        "Asam Nitrat (HNO3)": 1,
        "Asam Sulfat (H2SO4)": 2,
        "Asam Bromida (HBr)": 1,
        "Asam Bromit (HBrO3)": 1,
        "Asam Perbromat (HBrO4)": 1,
        "Asam Klorat (HClO3)": 1, 
        "Asam Perklorat (HClO4)": 1,
        "Asam Iodida (HI)": 1,
        "Asam Iodit (HIO3)": 1,
        "Asam Periodat (HIO4)": 1
    }

    selected_acid = st.selectbox(
        "Pilih senyawa asam", list(strong_acids.keys()))
    a = strong_acids[selected_acid]

    # Masukkan konsentrasi
    concentration = st.number_input(
        "Masukkan konsentrasi (M)", min_value=0.0, step=0.01)

    # Tombol hitung
    if st.button("Hitung"):
        H_plus, pH = calculate_strong_acid_pH(concentration, a)
        st.write("pH =", round(pH, 2))
        st.write("[H+] =", round(H_plus, 5))
        st.success(f"pH asam sebesar {pH:.2f}")

elif choice == "Menghitung dengan Konsentrasi Basa":
    st.subheader("Menghitung pH, pOH, dan [OH-] dari Konsentrasi Basa Kuat")

    # Pilih senyawa basa
    strong_bases = {
        "Natrium Hidroksida (NaOH)": 1,
        "Litium Hidroksida (LiOH)": 1,
        "Kalium Hidroksida (KOH)": 1,
        "Rubidium Hidroksida (RbOH)": 1,
        "Cesium Hidroksida (CsOH)": 1,
        "Kalsium Hidroksida (Ca(OH)2)": 2,
        "Barium Hidroksida (Ba(OH)2)": 2,
        "Stronsium Hidroksida (Sr(OH)2)": 2,
        "Magnesium Hidroksida (Mg(OH)2)": 2
    }

    selected_base = st.selectbox(
        "Pilih senyawa basa", list(strong_bases.keys()))
    a = strong_bases[selected_base]

    # Masukkan konsentrasi
    concentration = st.number_input(
        "Masukkan konsentrasi (M)", min_value=0.0, step=0.01)

    # Tombol hitung
    if st.button("Hitung"):
        OH_minus, pOH, pH = calculate_strong_base_pH(concentration, a)
        st.write("pH =", round(pH, 2))
        st.write("pOH =", round(pOH, 2))
        st.write("[OH-] =", round(OH_minus, 5))

elif choice == "Menghitung dengan Massa dan Volume asam":
    st.subheader("Menghitung pH dari Massa dan Volume Asam Kuat")

    strong_acids = {
        "Asam klorida (HCl) = 36,5 mg/mmol": 1,
        "Asam nitrat (HNO3) = 63,02 mg/mmol": 1,
        "Asam sulfat (H2SO4) = 98 mg/mmol": 2
    }

    selected_acid = st.selectbox(
        "Pilih senyawa asam", list(strong_acids.keys()))
    a = strong_acids[selected_acid]

    # Masukkan massa
    mass = st.number_input("Masukkan massa (mg)", min_value=0.0, step=0.1)

    # Masukkan volume
    volume = st.number_input("Masukkan volume (mL)", min_value=0.0, step=0.1)

    # Tombol hitung
    if st.button("Hitung"):
        # Konversi volume dari mL ke L
        volume_in_liters = volume / 1000
        H_plus, pH = calculate_strong_acid_mass_pH(mass, volume_in_liters, a)
        st.write("pH =", round(pH, 2))
        st.write("[H+] =", round(H_plus, 5))

elif choice == "Menghitung dengan Massa dan Volume Basa":
    st.subheader(
        "Menghitung pH, pOH, dan [OH-] dari Massa dan Volume Basa Kuat")

    strong_bases = {
        "Natrium hidroksida (NaOH)": 1,
        "Litium hidroksida (LiOH)": 1,
        "Kalium hidroksida (KOH)": 1
    }

    selected_base = st.selectbox(
        "Pilih senyawa basa", list(strong_bases.keys()))
    a = strong_bases[selected_base]

    # Masukkan massa
    mass = st.number_input("Masukkan massa (mg)", min_value=0.0, step=0.1)

    # Masukkan volume
    volume = st.number_input("Masukkan volume (mL)", min_value=0.0, step=0.1)

    # Tombol hitung
    if st.button("Hitung"):
        # Konversi volume dari mL ke L
        volume_in_liters = volume / 1000
        OH_minus, pOH, pH = calculate_strong_base_mass_pH(
            mass, volume_in_liters, a)
        st.write("pH =", round(pH, 2))
        st.write("pOH =", round(pOH, 2))
        st.write("[OH-] =", round(OH_minus, 5))

elif choice == "Menghitung dengan Massa dan Volume basa":
    st.subheader(
        "Menghitung pH, pOH, dan [OH-] dari Massa dan Volume Basa Kuat")

    # Pilih senyawa basa
    strong_bases = {
        "NaOH = 40 mg/mmol": 1,
        "Li(OH) = 259,47 mg/mmol": 1,
        "KOH = 56 mg/mmol": 1
    }

    selected_base = st.selectbox(
        "Pilih senyawa basa", list(strong_bases.keys()))
    valency = strong_bases[selected_base]

    # Masukkan massa dalam miligram
    mass = st.number_input("Masukkan massa (mg)", min_value=0.0, step=0.1)

    # Masukkan volume dalam mililiter
    volume = st.number_input("Masukkan volume (mL)", min_value=0.0, step=0.1)

    # Tombol hitung
    if st.button("Hitung"):
        OH_minus, pOH, pH = calculate_strong_base_mass_pH(
            mass, volume, valency)
        st.write("pH =", round(pH, 2))
        st.write("pOH =", round(pOH, 2))
        st.write("[OH-] =", round(OH_minus, 5))
