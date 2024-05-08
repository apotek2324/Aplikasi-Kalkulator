# Jalankan aplikasi dengan perintah `streamlit run filename.py`

import streamlit as st
import math


# Fungsi untuk menghitung pH untuk asam kuat

def perhitungan_pH_asam_kuat(konsentrasi, a):
    H_plus = konsentrasi * a
    pH = -math.log10(H_plus)
    return H_plus, pH


# Fungsi untuk menghitung pH untuk basa kuat

def perhitungan_pH_basa_kuat(konsentrasi, a):
    OH_minus = konsentrasi * a
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH


# Fungsi untuk menghitung pH untuk asam lemah

def perhitungan_pH_asam_lemah(ka, konsentrasi):
    H_plus = math.sqrt(ka * konsentrasi)
    pH = -math.log10(H_plus)
    return H_plus, pH


# Fungsi untuk menghitung pH untuk basa lemah

def perhitungan_pH_basa_lemah(kb, konsentrasi):
    OH_minus = math.sqrt(kb * konsentrasi)
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH


# Fungsi untuk menghitung pH dari massa dan volume untuk asam kuat

def perhitungan_pH_asam_kuat_dengan_massa_dan_volume(massa, volume, bm):
    H_plus = (massa / volume) * bm
    pH = -math.log10(H_plus)
    return H_plus, pH


# Fungsi untuk menghitung pH dari massa dan volume untuk asam lemah

def perhitungan_pH_asam_lemah_dengan_massa_dan_volume(massa dan volume):
    konsentrasi = (massa / volume)
    H_plus = Ka * konsentrasi
    akar = H_plus ** 0.5
    st.write('[H+] = ', akar)
    pH = -math.log10(H_plus)
    return H_plus, pH


# Fungsi untuk menghitung pH dari massa dan volume untuk basa kuat

def perhitungan_pH_basa_kuat_dengan_massa_dan_volume(massa, volume, bm):
    OH_minus = (massa / volume) * bm
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH


# Fungsi untuk menghitung pH dari massa dan volume untuk basa lemah

def perhitungan_pH_basa_lemah_dengan_massa_dan_volume(massa dan volume):
    konsentrasi = (massa / volume)
    OH_minus = Kb * konsentrasi
    akar = OH_minus ** 0.5
    st.write('[OH-] = ', akar)
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

    selected_asam = st.selectbox(
        "Pilih senyawa asam", list(asam_kuat.keys()))
    a = asam_kuat[selected_asam]

    # Masukkan konsentrasi
    konsentrasi = st.number_input(
        "Masukkan konsentrasi (M)", min_value=0.0000, step=0.0000)

    # Tombol hitung
    if st.button("Hitung"):
        H_plus, pH = perhitungan_pH_asam_kuat(konsentrasi, a)
        st.write("[H+] =", round(H_plus, 4))
        st.write("pH =", round(pH, 2))
        st.success(f'pH asam adalah {pH:.2f}')


elif choice == "Menghitung dengan Konsentrasi Asam Lemah":
    st.subheader("Menghitung pH dan [H+] dari Konsentrasi Asam Lemah")

    # Masukkan konsentrasi dan Ka
    konstanta_asam = st.number_input('Masukkan Ka')
    st.write("Ka = ", konstanta_asam)
    konsentrasi = st.number_input('Masukkan konsentrasi')
    st.write("konsentrasi = ", konsentrasi)
    
    # Tombol hitung
    hitung = st.button('Hitung pH')
    if st.button ("Hitung"):
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

    selected_basa = st.selectbox(
        "Pilih senyawa basa", list(basa_kuat.keys()))
    a = basa_kuat[selected_basa]

    # Masukkan konsentrasi
    konsentrasi = st.number_input(
        "Masukkan konsentrasi (M)", min_value=0.0000, step=0.0000)

    # Tombol hitung
    if st.button("Hitung"):
        OH_minus, pOH, pH = perhitungan_pH_basa_kuat(konsentrasi, a)
        st.write("[OH-] =", round(OH_minus, 5))
        st.write("pOH =", round(pOH, 2))
        st.write("pH =", round(pH, 2))
        st.success(f'pH basa adalah {pH:.2f}')
        

elif choice == "Menghitung dengan Konsentrasi Basa Lemah":
    st.subheader("Menghitung pH, pOH, dan [OH-] dari Konsentrasi Basa Lemah")

    # Masukkan konsentrasi dan Kb
    konstanta_basa = st.number_input('Masukkan Kb')
    st.write("Kb = ", konstanta_basa)
    konsentrasi = st.number_input('Masukkan konsentrasi')
    st.write("konsentrasi = ", konsentrasi)
    
    # Tombol hitung
    hitung = st.button('Hitung pH')
    if st.button ("Hitung"):
        OH_minus, pH = perhitungan_pH_basa_lemah(konsentrasi, Kb)
        st.write("[OH-] =", round(OH_minus, 4))
        st.write("pOH =", round(pOH, 2))
        st.write("pH =", round(pH, 2))
        st.success(f'pH basa adalah {pH:.2f}')


elif choice == "Menghitung dengan Massa dan Volume asam kuat":
    st.subheader("Menghitung pH dari Massa dan Volume Asam Kuat")

    asam_kuat = {
        "Asam Klorida (HCl) = 36,5 g/mol",
        "Asam Nitrat (HNO3) = 63,02 g/mol",
        "Asam Sulfat (H2SO4) = 98 g/mol"
        "Asam Bromida (HBr) = 81 g/mol",
        "Asam Bromit (HBrO3) = 128,9 g/mol",
        "Asam Perbromat (HBrO4) = 146 g/mol",
        "Asam Klorat (HClO3) = 84,5 g/mol", 
        "Asam Perklorat (HClO4) = 100,5 g/mol",
        "Asam Iodida (HI) = 128 g/mol",
        "Asam Iodit (HIO3) = 176 g/mol",
        "Asam Periodat (HIO4) = 192 g/mol"
    }

    selected_acid = st.selectbox(
        "Pilih senyawa asam", list(strong_acids.keys()))
    a = strong_acids[selected_acid]

    # Masukkan massa
    mass = st.number_input("Masukkan massa (mg)", min_value=0.00, step=0.10)

    # Masukkan volume
    volume = st.number_input("Masukkan volume (mL)", min_value=0.00, step=0.10)

    # Tombol hitung
    if st.button("Hitung"):
        # Konversi volume dari mL ke L
        volume_dalam_liter = volume / 1000
        H_plus, pH = perhitungan_pH_asam_kuat_dengan_massa_dan_volume(massa, volume_dalam_liter, a)
        st.write("[H+] =", round(H_plus, 4))
        st.write("pH =", round(pH, 2))
        st.success(f'pH asam adalah {pH:.2f}')


elif choice == "Menghitung dengan Massa dan Volume Basa Kuat":
    st.subheader(
        "Menghitung pH, pOH, dan [OH-] dari Massa dan Volume Basa Kuat")

    basa_kuat = {
        "Natrium Hidroksida (NaOH) = 40 g/mol",
        "Litium Hidroksida (LiOH) = 259,47 g/mol",
        "Kalium Hidroksida (KOH) = 56 g/mol",
        "Rubidium Hidroksida (RbOH) =",
        "Cesium Hidroksida (CsOH) =",
        "Kalsium Hidroksida (Ca(OH)2) =",
        "Barium Hidroksida (Ba(OH)2) =",
        "Stronsium Hidroksida (Sr(OH)2) =",
        "Magnesium Hidroksida (Mg(OH)2) ="
    }

    selected_basa = st.selectbox(
        "Pilih senyawa basa kuat", list(basa_kuat.keys()))
    a = basa_kuat[selected_basa]

    # Masukkan massa
    massa = st.number_input("Masukkan massa (mg)", min_value=0.00, step=0.10)

    # Masukkan volume
    volume = st.number_input("Masukkan volume (mL)", min_value=0.00, step=0.10)

    # Tombol hitung
    if st.button("Hitung"):
        # Konversi volume dari mL ke L
        volume_dalam_liter = volume / 1000
        OH_minus, pOH, pH = perhitungan_pH_basa_kuat_dengan_massa_dan_volume(
            massa, volume_dalam_liter, a)
        st.write("[OH-] =", round(OH_minus, 5))
        st.write("pOH =", round(pOH, 2))
        st.write("pH =", round(pH, 2))
        st.success(f'pH basa adalah {pH:.2f}')


