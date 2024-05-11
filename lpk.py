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

def perhitungan_pH_asam_lemah(Konstanta_asam, Konsentrasi):
    H_plus = math.sqrt(Konstanta_asam * Konsentrasi)
    pH = -math.log10(H_plus)
    return H_plus, pH
    
# Fungsi untuk menghitung pH basa lemah

def perhitungan_pH_basa_lemah(Konstanta_basa, Konsentrasi):
    OH_minus = math.sqrt(Konstanta_basa * Konsentrasi)
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH

# Fungsi untuk menghitung pH asam kuat dengan massa, volume, dan BM 

def perhitungan_pH_asam_kuat_dengan_massa_volume_BM(massa, volume_dalam_liter, BM, a):
    Konsentrasi = massa / (volume_dalam_liter * BM)
    H_plus = Konsentrasi * a
    pH = -math.log10(H_plus)
    return H_plus, pH
    
# Fungsi untuk menghitung pH basa kuat dengan massa, volume, dan BM 

def perhitungan_pH_basa_kuat_dengan_massa_volume_BM(massa, volume_dalam_liter, BM, a):
    Konsentrasi = massa / (volume_dalam_liter * BM)
    OH_minus = Konsentrasi * a
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH
    
# Fungsi untuk menghitung pH asam lemah dengan massa, volume, dan BM 

def perhitungan_pH_asam_lemah_dengan_massa_volume_BM(massa, volume_dalam_liter, BM, Konstanta_asam):
    Konsentrasi = massa / (volume_dalam_liter * BM)
    H_plus = math.sqrt(Konstanta_asam * Konsentrasi)
    pH = -math.log10(H_plus)
    return H_plus, pH

# Fungsi untuk menghitung pH basa lemah dengan massa, volume, dan BM 

def perhitungan_pH_basa_lemah_dengan_massa_volume_BM(massa, volume_dalam_liter, BM, Konstanta_basa):
    Konsentrasi = (massa / (volume_dalam_liter * BM)) 
    OH_minus = math.sqrt(Konstanta_basa * Konsentrasi)
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH
    
# Judul aplikasi
st.title("Kalkulator pH Larutan")

# Halaman utama untuk pilihan
options = ["Beranda",
           "Konsentrasi Asam",
           "Konsentrasi Basa",
           "Massa dan Volume Asam",
           "Massa dan Volume Basa",
           "About This App"
          ]

choice = st.sidebar.radio("Pilih Metode", options)

if choice == "Beranda":
    st.subheader("Menghitung [H+] dan pH dari Konsentrasi Asam Kuat dan Asam Lemah")

elif choice == "Konsentrasi Asam":
    st.subheader("Menghitung [H+] dan pH dari Konsentrasi Asam Kuat dan Asam Lemah")

    tab1, tab2 = st.tabs(["Asam Kuat", "Asam Lemah"])

    with tab1:
        st.header("Asam Kuat")
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
        st.write("a = ", a)
        
        # Masukkan konsentrasi
        Konsentrasi = st.number_input(
            "Masukkan konsentrasi (M)", format = "%.4f", step=0.0001, key = "H1")
        st.write("Konsentrasi = ", Konsentrasi)
        
        # Tombol hitung
        if st.button("Hitung pH", key = "B1"):
            H_plus, pH = perhitungan_pH_asam_kuat(Konsentrasi, a)
            st.write("[H+] =", round(H_plus, 4))
            st.write("pH =", round(pH, 2))            
            st.success(f'pH asam adalah {pH:.2f}')

    with tab2:
        st.header("Asam Lemah")

        # Masukkan Ka
        Konstanta_asam = st.number_input('Masukkan Ka')
        st.write("Ka = ", Konstanta_asam)

        # Masukkan konsentrasi
        Konsentrasi = st.number_input('Masukkan konsentrasi (M)', format = "%.4f", step=0.0001, key = "H2")
        st.write("Konsentrasi = ", Konsentrasi )
        
        # Tombol hitung
        if st.button ("Hitung pH", key = "B2"):
            H_plus, pH = perhitungan_pH_asam_lemah(Konsentrasi_lemah, Konstanta_asam)
            st.write("[H+] =", round(H_plus, 4))
            st.write("pH =", round(pH, 2))
            st.success(f'pH asam adalah {pH:.2f}')

elif choice == "Konsentrasi Basa":
    st.subheader("Menghitung [OH-], pOH, dan pH dari Konsentrasi Basa Kuat dan Basa Lemah")

    tab1, tab2 = st.tabs(["Basa Kuat", "Basa Lemah"])

    with tab1:
        st.header("Basa Kuat")
        
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
        st.write("a = ", a)
    
        # Masukkan konsentrasi
        Konsentrasi = st.number_input(
            "Masukkan konsentrasi (M)", format= "%.4f", step=0.0001, key = "H3")
        st.write("Konsentrasi = ", Konsentrasi)
    
        # Tombol hitung
        if st.button("Hitung pH", key = "B3"):
            OH_minus, pOH, pH = perhitungan_pH_basa_kuat(Konsentrasi, a)
            st.write("[OH-] =", round(OH_minus, 4))
            st.write("pOH =", round(pOH, 2))
            st.write("pH =", round(pH, 2))
            st.success(f'pH basa adalah {pH:.2f}')

    with tab2:
        st.header("Basa Lemah")

        # Masukkan Kb
        Konstanta_basa = st.number_input('Masukkan Kb')
        st.write("Kb = ", Konstanta_basa)
    
        # Masukkan konsentrasi
        Konsentrasi = st.number_input('Masukkan konsentrasi (M)', format = "%.4f", step=0.0001, key = "H4")
        st.write("Konsentrasi = ", Konsentrasi)
        
        # Tombol hitung
        if st.button ("Hitung pH", key = "B4"):
            OH_minus, pOH, pH = perhitungan_pH_basa_lemah(Konsentrasi, Konstanta_basa)
            st.write("[OH-] =", round(OH_minus, 4))
            st.write("pOH =", round(pOH, 2))
            st.write("pH =", round(pH, 2))
            st.success(f'pH basa adalah {pH:.2f}')


elif choice == "Massa dan Volume Asam":
    st.subheader("Menghitung [H+] dan pH dari Massa dan Volume Asam Kuat dan Asam Lemah")

    tab1, tab2 = st.tabs(["Asam Kuat", "Asam Lemah"])

    with tab1:
        st.header("Asam Kuat")
        
        # Pilih senyawa asam kuat
        asam_kuat = {
            "Asam Klorida (HCl)":(36.5, 1),
            "Asam Nitrat (HNO3)":(63, 1),
            "Asam Sulfat (H2SO4)":(98, 2),
            "Asam Bromida (HBr)":(81, 1),
            "Asam Bromit (HBrO3)":(129, 1),
            "Asam Perbromat (HBrO4)":(145, 1),
            "Asam Klorat (HClO3)":(84.5, 1),
            "Asam Perklorat (HClO4)":(100.46, 1),
            "Asam Iodida (HI)":(127.91, 1),
            "Asam Iodit (HIO3)":(175.91, 1),
            "Asam Periodat (HIO4)":(191.91, 1)
        }
    
        selected_asam_kuat = st.selectbox(
            "Pilih senyawa asam kuat", list(asam_kuat.keys()))
        BM = asam_kuat[selected_asam_kuat][0]
        a = asam_kuat[selected_asam_kuat][1]
        st.write("BM = ", BM, "g/mol") 
        st.write("a = ", a) 
        
        # Masukkan massa
        massa = st.number_input("Masukkan massa (g)", format= "%.4f", step=0.0001, key = "M5")
        st.write("Massa = ", massa)
    
        # Masukkan volume
        volume = st.number_input("Masukkan volume (mL)", key = "V5")
        st.write("Volume = ", volume)
    
        # Tombol hitung
        if st.button("Hitung pH", key = "B5"):
            # Konversi volume dari mL ke L
            volume_dalam_liter = volume / 1000
            H_plus, pH = perhitungan_pH_asam_kuat_dengan_massa_volume_BM(massa, volume_dalam_liter, BM, a)
            st.write("[H+] =", round(H_plus, 4))
            st.write("pH =", round(pH, 2))
            st.success(f'pH asam adalah {pH:.2f}')

    with tab2:
        st.header("Asam Lemah")
        
        # Pilih senyawa asam lemah
        asam_lemah = {
            "Asam Asetat (CH3COOH)": 60,
            "Asam Fluorida (HF)": 20,
            "Asam Sianida (HCN)": 27,
            "Asam Sulfida (H2S)": 32,
            "Asam Sulfit (H2SO3)": 82.1,
            "Asam Fosfat (H3PO4)": 98,
            "Asam Karbonat (H2CO3)": 62,
            "Asam Hipoklorit (HClO)": 52.5,
            "Asam Nitrit (HNO2)": 47 
        }
        
        selected_asam_lemah = st.selectbox(
            "Pilih senyawa asam lemah", list(asam_lemah.keys()))
        BM = asam_lemah[selected_asam_lemah]
        st.write("BM = ", BM, "g/mol") 
    
        # Masukkan Ka
        Konstanta_asam = st.number_input('Masukkan Ka', key = "K6")
        st.write("Ka = ", Konstanta_asam)
        
        # Masukkan massa
        massa = st.number_input("Masukkan massa (g)", format= "%.4f", step=0.0001, key = "M6")
        st.write("Massa = ", massa)
    
        # Masukkan volume
        volume = st.number_input("Masukkan volume (mL)", key = "V6")
        st.write("Volume = ", volume)
    
        # Tombol hitung
        if st.button("Hitung pH", key = "B6"):
            # Konversi volume dari mL ke L
            volume_dalam_liter = volume / 1000
            H_plus, pH = perhitungan_pH_asam_lemah_dengan_massa_volume_BM(massa, volume_dalam_liter, BM, Konstanta_asam)
            st.write("[H+] =", round(H_plus, 4))
            st.write("pH =", round(pH, 2))
            st.success(f'pH asam adalah {pH:.2f}')

elif choice == "Massa dan Volume Basa":
    st.subheader(
        "Menghitung [OH-], pOH, dan pH dari Massa dan Volume Basa Kuat dan Basa Lemah")

    tab1, tab2 = st.tabs(["Basa Kuat", "Basa Lemah"])

    with tab1:
        st.header("Basa Kuat")

        # Pilih senyawa basa kuat
        basa_kuat = {
            "Natrium Hidroksida (NaOH)":(40, 1),
            "Litium Hidroksida (LiOH)":(23.95, 1),
            "Kalium Hidroksida (KOH)":(56.1, 1),
            "Rubidium Hidroksida (RbOH)":(102.48, 1),
            "Cesium Hidroksida (CsOH)":(149.91, 1),
            "Kalsium Hidroksida (Ca(OH)2)":(74, 2),
            "Barium Hidroksida (Ba(OH)2)":(171.34, 2),
            "Stronsium Hidroksida (Sr(OH)2)":(121.63, 2),
            "Magnesium Hidroksida (Mg(OH)2)":(58.32, 2)
        }
        
        selected_basa_kuat = st.selectbox(
            "Pilih senyawa basa kuat", list(basa_kuat.keys()))
        BM = basa_kuat[selected_basa_kuat][0]
        a = basa_kuat[selected_basa_kuat][1]
        st.write("BM = ", BM, "g/mol") 
        st.write("a = ", a) 
        
        # Masukkan massa
        massa = st.number_input("Masukkan massa (g)", format= "%.4f", step=0.0001, key = "M7")
        st.write("Massa = ", massa)
    
        # Masukkan volume
        volume = st.number_input("Masukkan volume (mL)")
        st.write("Volume = ", volume)
    
        # Tombol hitung
        if st.button("Hitung pH"):
            # Konversi volume dari mL ke L
            volume_dalam_liter = volume / 1000
            OH_minus, pOH, pH = perhitungan_pH_basa_kuat_dengan_massa_volume_BM(
                massa, volume_dalam_liter, BM, a)
            st.write("[OH-] =", round(OH_minus, 5))
            st.write("pOH =", round(pOH, 2))
            st.write("pH =", round(pH, 2))
            st.success(f'pH basa adalah {pH:.2f}')
    
    with tab2:
        st.header("Basa Lemah")

        # Pilih senyawa basa lemah
        basa_lemah = {
            "Ammonium Hidroksida (NH4OH)": 35,
            "Perak Hidroksida (AgOH)": 125,
            "Seng Hidroksida (Zn(OH)2)": 99.42, 
            "Nikel Hidroksida (Ni(OH)2)": 91,
            "Alluminium (III) Hidroksida (Al(OH)3)": 78,  
            "Bismuth Hidroksida (Bi(OH)3)": 260,
            "Besi (II) Hidroksida (Fe(OH)2)": 89.86,
            "Besi (III) Hidroksida (Fe(OH)3)": 107,
            "Kobalt (II) Hidroksida (Co(OH)2)": 92.95,
            "Kobalt (III) Hidroksida (Co(OH)3)": 109.96, 
            "Raksa (I) Hidroksida (HgoH)": 218,
            "Raksa (II) Hidroksida (Hg(OH)2)": 252,
            "Tembaga (I) Hidroksida (CuOH)": 80.5,
            "Tembaga (II) Hidroksida (Cu(OH)2)": 44.01
        }
        
        selected_basa_lemah = st.selectbox(
            "Pilih senyawa basa lemah", list(basa_lemah.keys()))
        BM = basa_lemah[selected_basa_lemah]
        st.write("BM = ", BM, "g/mol") 
    
        # Masukkan Kb
        Konstanta_basa = st.number_input('Masukkan Kb', key = "K8")
        st.write("Kb = ", Konstanta_basa)
        
        # Masukkan massa
        massa = st.number_input("Masukkan massa (g)", format= "%.4f", step=0.0001, key = "M8")
        st.write("Massa = ", massa)
    
        # Masukkan volume
        volume = st.number_input("Masukkan volume (mL)", key = "V8")
        st.write("Volume = ", volume)
        
        # Tombol hitung
        if st.button("Hitung pH", key = "B8"):
            # Konversi volume dari mL ke L
            volume_dalam_liter = volume / 1000
            OH_minus, pOH, pH = perhitungan_pH_basa_lemah_dengan_massa_volume_BM(
                massa, volume_dalam_liter, BM, Konstanta_basa)
            st.write("[OH-] =", round(OH_minus, 5))
            st.write("pOH =", round(pOH, 2))
            st.write("pH =", round(pH, 2))
            st.success(f'pH basa adalah {pH:.2f}')

elif choice == "About This App":
    #Apa itu pH
    st.subheader("Apa itu pH?")
    st.write('pH adalah ukuran keasaman atau kebasaan suatu larutan kimia. pH adalah nilai numerik yang menyatakan seberapa asam atau basa suatu larutan cair.')

    #Skala pH
    st.subheader("Skala pH")
    st.write('pH diukur pada skala mulai dari 0 hingga 14. PH 7 dianggap netral. Air murni, atau larutan berair yang hanya mengandung bahan kimia netral, akan memiliki pH 7. Nilai yang lebih rendah dari 7 bersifat asam, dan semakin rendah nilai pH, semakin asam larutan tersebut. Nilai yang lebih tinggi dari 7 bersifat basa, dan nilai yang lebih tinggi berarti lebih basa.'
            )
    st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fid%2Fvektor%2Fskala-ph-ph-indikator-universal-strip-uji-gm954645674-260647627&psig=AOvVaw1kl1bznlexd8KBKTlNi_xN&ust=1715487167170000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCIj8zJTehIYDFQAAAAAdAAAAABAE")

    #Cara Menggunakan Kalkulator pH
    st.subheader("Cara Menggunakan Kalkulator pH")
   
