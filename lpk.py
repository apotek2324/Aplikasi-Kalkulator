# Jalankan aplikasi dengan perintah `streamlit run filename.py`

import streamlit as st
import math

# Fungsi untuk menghitung pH asam kuat

def perhitungan_pH_asam_kuat(Konsentrasi, a):
    H_plus = Konsentrasi * a
    pH = -math.log10(H_plus)
    return H_plus, pH

# Fungsi untuk menghitung pH basa kuat

def perhitungan_pH_basa_kuat(Konsentrasi, a):
    OH_minus = Konsentrasi * a
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH

# Fungsi untuk menghitung pH asam lemah

def perhitungan_pH_asam_lemah(Ka, Konsentrasi):
    H_plus = math.sqrt(Ka * Konsentrasi)
    pH = -math.log10(H_plus)
    return H_plus, pH

# Fungsi untuk menghitung pH basa lemah

def perhitungan_pH_basa_lemah(Kb, Konsentrasi):
    OH_minus = math.sqrt(Kb * Konsentrasi)
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH

# Fungsi untuk menghitung pH dari massa dan volume untuk basa kuat

def perhitungan_konsentrasi_dengan_massa_volume_BM(massa, volume, BM):
    OH_minus = massa / (volume * BM)
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH

# Judul aplikasi
st.title("Kalkulator Perhitungan pH Larutan")

# Halaman utama untuk pilihan
options = ["Menghitung dengan Konsentrasi Asam Kuat",
           "Menghitung dengan Konsentrasi Asam Lemah",
           "Menghitung dengan Konsentrasi Basa Kuat",
           "Menghitung dengan Konsentrasi Basa Lemah",
           "Menghitung dengan Massa dan Volume Asam Kuat",
           "Menghitung dengan Massa dan Volume Asam Lemah",
           "Menghitung dengan Massa dan Volume Basa Kuat",
           "Menghitung dengan Massa dan Volume Basa Lemah"
          ]

choice = st.sidebar.radio("Pilih Metode", options)

if choice == "Menghitung dengan Konsentrasi Asam Kuat":
    st.subheader("Menghitung pH dan [H+] dari Konsentrasi Asam Kuat")

    # Pilih senyawa asam kuat
    asam_kuat = {
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

    selected_asam_kuat = st.selectbox(
        "Pilih senyawa asam kuat", list(asam_kuat.keys()))
    a = asam_kuat[selected_asam_kuat]

    # Masukkan konsentrasi
    Konsentrasi = st.number_input(
        "Masukkan konsentrasi (M)", min_value=0.0000, step=0.0000)

    # Tombol hitung
    if st.button("Hitung pH"):
        H_plus, pH = perhitungan_pH_asam_kuat(konsentrasi, a)
        st.write("[H+] =", round(H_plus, 4))
        st.write("pH =", round(pH, 2))
        st.success(f'pH asam adalah {pH:.2f}')

elif choice == "Menghitung dengan Konsentrasi Asam Lemah":
    st.subheader("Menghitung pH dan [H+] dari Konsentrasi Asam Lemah")

    # Masukkan konsentrasi dan Ka
    Konstanta_asam = st.number_input('Masukkan Ka')
    st.write("Ka = ", Konstanta_asam)
    Konsentrasi = st.number_input('Masukkan konsentrasi')
    st.write("Konsentrasi = ", Konsentrasi)
    
    # Tombol hitung
    if st.button ("Hitung pH"):
        H_plus, pH = perhitungan_pH_asam_lemah(konsentrasi, Ka)
        st.write("[H+] =", round(H_plus, 4))
        st.write("pH =", round(pH, 2))
        st.success(f'pH asam adalah {pH:.2f}')

elif choice == "Menghitung dengan Konsentrasi Basa Kuat":
    st.subheader("Menghitung [OH-], pOH, dan pH dari Konsentrasi Basa Kuat")

    # Pilih senyawa basa kuat
    basa_kuat = {
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

    selected_basa_kuat = st.selectbox(
        "Pilih senyawa basa kuat", list(basa_kuat.keys()))
    a = basa_kuat[selected_basa_kuat]

    # Masukkan konsentrasi
    konsentrasi = st.number_input(
        "Masukkan konsentrasi (M)", min_value=0.0000, step=0.0000)

    # Tombol hitung
    if st.button("Hitung pH"):
        OH_minus, pOH, pH = perhitungan_pH_basa_kuat(konsentrasi, a)
        st.write("[OH-] =", round(OH_minus, 5))
        st.write("pOH =", round(pOH, 2))
        st.write("pH =", round(pH, 2))
        st.success(f'pH basa adalah {pH:.2f}')

elif choice == "Menghitung dengan Konsentrasi Basa Lemah":
    st.subheader("Menghitung pH, pOH, dan [OH-] dari Konsentrasi Basa Lemah")

    # Masukkan konsentrasi dan Kb
    Konstanta_basa = st.number_input('Masukkan Kb')
    st.write("Kb = ", Konstanta_basa)
    Konsentrasi = st.number_input('Masukkan konsentrasi')
    st.write("Konsentrasi = ", Konsentrasi)
    
    # Tombol hitung
    if st.button ("Hitung pH"):
        OH_minus, pH = perhitungan_pH_basa_lemah(Konsentrasi, Kb)
        st.write("[OH-] =", round(OH_minus, 4))
        st.write("pOH =", round(pOH, 2))
        st.write("pH =", round(pH, 2))
        st.success(f'pH basa adalah {pH:.2f}')


elif choice == "Menghitung dengan Massa dan Volume asam kuat":
    st.subheader("Menghitung pH dari Massa dan Volume Asam Kuat")

    asam_kuat = {
        "Asam Klorida (HCl) = 36,5 g/mol": 36.5,
        "Asam Nitrat (HNO3) = 63,02 g/mol": 63.02,
        "Asam Sulfat (H2SO4) = 98 g/mol": 98,
        "Asam Bromida (HBr) = 81 g/mol": 81,
        "Asam Bromit (HBrO3) = 128,9 g/mol": 128.9,
        "Asam Perbromat (HBrO4) = 146 g/mol": 146,
        "Asam Klorat (HClO3) = 84,5 g/mol": 84.5, 
        "Asam Perklorat (HClO4) = 100,5 g/mol": 100.5,
        "Asam Iodida (HI) = 128 g/mol": 128,
        "Asam Iodit (HIO3) = 176 g/mol": 176,
        "Asam Periodat (HIO4) = 192 g/mol": 192
    }

    selected_asam_kuat = st.selectbox(
        "Pilih senyawa asam kuat", list(asam_kuat.keys()))
    BM = asam_kuat[selected_asam_kuat]

    # Masukkan massa
    massa = st.number_input("Masukkan massa (g)", min_value=0.00, step=0.10)

    # Masukkan volume
    volume = st.number_input("Masukkan volume (mL)", min_value=0.00, step=0.10)

    # Tombol hitung
    if st.button("Hitung"):
        # Konversi volume dari mL ke L
        volume_dalam_liter = volume / 1000
        H_plus, pH = perhitungan_konsentrasi_dengan_massa_volume_BM(massa, volume_dalam_liter, BM)
        st.write("[H+] =", round(H_plus, 4))
        st.write("pH =", round(pH, 2))
        st.success(f'pH asam adalah {pH:.2f}')

elif choice == "Menghitung dengan Massa dan Volume Basa Kuat":
    st.subheader(
        "Menghitung pH, pOH, dan [OH-] dari Massa dan Volume Basa Kuat")

    basa_kuat = {
        "Natrium Hidroksida (NaOH) = 40 g/mol": 40,
        "Litium Hidroksida (LiOH) = 259,47 g/mol": 259.47,
        "Kalium Hidroksida (KOH) = 56 g/mol": 56,
        "Rubidium Hidroksida (RbOH) =": 32,
        "Cesium Hidroksida (CsOH) =":45 ,
        "Kalsium Hidroksida (Ca(OH)2) =": 35,
        "Barium Hidroksida (Ba(OH)2) =": 12,
        "Stronsium Hidroksida (Sr(OH)2) =": 21,
        "Magnesium Hidroksida (Mg(OH)2) =": 20 
    }
    
    selected_basa_kuat = st.selectbox(
        "Pilih senyawa basa kuat", list(basa_kuat.keys()))
    BM = basa_kuat[selected_basa_kuat]
    
    # Masukkan massa
    massa = st.number_input("Masukkan massa (g)", min_value=0.00, step=0.10)

    # Masukkan volume
    volume = st.number_input("Masukkan volume (mL)", min_value=0.00, step=0.10)

    # Tombol hitung
    if st.button("Hitung"):
        # Konversi volume dari mL ke L
        volume_dalam_liter = volume / 1000
        OH_minus, pOH, pH = perhitungan_konsentrasi_dengan_massa_volume_BM(
            massa, volume_dalam_liter, BM)
        st.write("[OH-] =", round(OH_minus, 5))
        st.write("pOH =", round(pOH, 2))
        st.write("pH =", round(pH, 2))
        st.success(f'pH basa adalah {pH:.2f}')


