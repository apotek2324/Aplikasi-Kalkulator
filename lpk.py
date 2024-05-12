# Jalankan aplikasi dengan perintah `streamlit run filename.py`

import streamlit as st
import math

st.set_page_config(page_title="Kalkulator pH", page_icon=":1234:", layout="wide")

# Fungsi untuk menghitung pH asam kuat

def perhitungan_pH_asam_kuat(konsentrasi, a):
    H_plus = konsentrasi * a
    pH = -math.log10(H_plus)
    return H_plus, pH

# Fungsi untuk menghitung pH basa kuat

def perhitungan_pH_basa_kuat(konsentrasi, a):
    OH_minus = konsentrasi * a
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH

# Fungsi untuk menghitung pH asam lemah

def perhitungan_pH_asam_lemah(konstanta_asam, konsentrasi):
    H_plus = math.sqrt(konstanta_asam * konsentrasi)
    pH = -math.log10(H_plus)
    return H_plus, pH
    
# Fungsi untuk menghitung pH basa lemah

def perhitungan_pH_basa_lemah(konstanta_basa, konsentrasi):
    OH_minus = math.sqrt(konstanta_basa * konsentrasi)
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH

# Fungsi untuk menghitung pH asam kuat dengan massa, volume, dan BM 

def perhitungan_pH_asam_kuat_dengan_massa_volume_BM(massa, volume_dalam_liter, BM, a):
    konsentrasi = massa / (volume_dalam_liter * BM)
    H_plus = konsentrasi * a
    pH = -math.log10(H_plus)
    return H_plus, pH
    
# Fungsi untuk menghitung pH basa kuat dengan massa, volume, dan BM 

def perhitungan_pH_basa_kuat_dengan_massa_volume_BM(massa, volume_dalam_liter, BM, a):
    konsentrasi = massa / (volume_dalam_liter * BM)
    OH_minus = konsentrasi * a
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH
    
# Fungsi untuk menghitung pH asam lemah dengan massa, volume, dan BM 

def perhitungan_pH_asam_lemah_dengan_massa_volume_BM(massa, volume_dalam_liter, BM, Konstanta_asam):
    konsentrasi = massa / (volume_dalam_liter * BM)
    H_plus = math.sqrt(konstanta_asam * konsentrasi)
    pH = -math.log10(H_plus)
    return H_plus, pH

# Fungsi untuk menghitung pH basa lemah dengan massa, volume, dan BM 

def perhitungan_pH_basa_lemah_dengan_massa_volume_BM(massa, volume_dalam_liter, BM, Konstanta_basa):
    konsentrasi = (massa / (volume_dalam_liter * BM)) 
    OH_minus = math.sqrt(konstanta_basa * konsentrasi)
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
    st.header('👨‍🔬SELAMAT DATANG👩‍🔬')
    st.markdown('---')
    st.write('Aplikasi ini dibuat untuk memudahkan dalam menghitung pH suatu larutan. Silakan pilih metode perhitungan yang sesuai, kemudian ikuti perintah yang ditampilkan di layar.')
    st.markdown('---')
    st.subheader('KELOMPOK 2 (1D - ANALISIS KIMIA)')
    st.write('''ANGGOTA KELOMPOK:
1. Fairuz Zahrany De Shaula    (2360)
2. Kesya Melia Adriani         (2360)
3. Reza Imelda                 (2360) 
4. Riska Maulidya Ainy         (2360242) 
5. Talitha Syahla Kurniawan    (2360)
''')
    
elif choice == "Konsentrasi Asam":
    st.subheader("Menghitung [H+] dan pH dari Konsentrasi Asam Kuat dan Asam Lemah")

    tab1, tab2, tab3 = st.tabs(["Asam Kuat", "Asam Lemah", "Custom"])

    with tab1:
        st.subheader("Asam Kuat")
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
        konsentrasi = st.number_input(
            "Masukkan konsentrasi (M)", format = "%.4f", step=0.0001, key = "H1")
        st.write("Konsentrasi = ", konsentrasi)
        
        # Tombol hitung
        if st.button("Hitung pH", key = "B1"):
            H_plus, pH = perhitungan_pH_asam_kuat(konsentrasi, a)
            st.write("[H+] =", round(H_plus, 4))
            st.write("pH =", round(pH, 2))            
            st.success(f'pH asam adalah {pH:.2f}')

    with tab2:
        st.subheader("Asam Lemah")

        # Masukkan Ka
        konstanta_asam = st.number_input('Masukkan Ka')
        st.write("Ka = ", konstanta_asam)

        # Masukkan konsentrasi
        konsentrasi = st.number_input('Masukkan konsentrasi (M)', format = "%.4f", step=0.0001, key = "H2")
        st.write("Konsentrasi = ", konsentrasi )
        
        # Tombol hitung
        if st.button ("Hitung pH", key = "B2"):
            H_plus, pH = perhitungan_pH_asam_lemah(konsentrasi, konstanta_asam)
            st.write("[H+] =", round(H_plus, 4))
            st.write("pH =", round(pH, 2))
            st.success(f'pH asam adalah {pH:.2f}')

    with tab3:
        options = ("Asam Kuat", "Asam Lemah")
        selection = st.selectbox("Pilih jenis senyawa", options=options)
        if selection == "Asam Kuat": 
            # Masukkan konsentrasi
            konsentrasi = st.number_input(
                "Masukkan konsentrasi (M)", format = "%.4f", step=0.0001, key = "H")
            st.write("Konsentrasi = ", konsentrasi)
            
            # Tombol hitung
            if st.button("Hitung pH", key = "Bu"):
                H_plus, pH = perhitungan_pH_asam_kuat(konsentrasi, a)
                st.write("[H+] =", round(H_plus, 4))
                st.write("pH =", round(pH, 2))            
                st.success(f'pH asam adalah {pH:.2f}')

            elif selection == "Asam Lemah":
                # Masukkan Ka
                konstanta_asam = st.number_input('Masukkan Ka')
                st.write("Ka = ", konstanta_asam)
        
                # Masukkan konsentrasi
                konsentrasi = st.number_input('Masukkan konsentrasi (M)', format = "%.4f", step=0.0001, key = "Ho")
                st.write("Konsentrasi = ", konsentrasi )
                
                # Tombol hitung
                if st.button ("Hitung pH", key = "Bp"):
                    H_plus, pH = perhitungan_pH_asam_lemah(konsentrasi, konstanta_asam)
                    st.write("[H+] =", round(H_plus, 4))
                    st.write("pH =", round(pH, 2))
                    st.success(f'pH asam adalah {pH:.2f}')


elif choice == "Konsentrasi Basa":
    st.subheader("Menghitung [OH-], pOH, dan pH dari Konsentrasi Basa Kuat dan Basa Lemah")

    tab1, tab2 = st.tabs(["Basa Kuat", "Basa Lemah"])

    with tab1:
        st.subheader("Basa Kuat")
        
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
        konsentrasi = st.number_input(
            "Masukkan konsentrasi (M)", format= "%.4f", step=0.0001, key = "H3")
        st.write("Konsentrasi = ", konsentrasi)
    
        # Tombol hitung
        if st.button("Hitung pH", key = "B3"):
            OH_minus, pOH, pH = perhitungan_pH_basa_kuat(konsentrasi, a)
            st.write("[OH-] =", round(OH_minus, 4))
            st.write("pOH =", round(pOH, 2))
            st.write("pH =", round(pH, 2))
            st.success(f'pH basa adalah {pH:.2f}')

    with tab2:
        st.subheader("Basa Lemah")

        # Masukkan Kb
        konstanta_basa = st.number_input('Masukkan Kb')
        st.write("Kb = ", konstanta_basa)
    
        # Masukkan konsentrasi
        konsentrasi = st.number_input('Masukkan konsentrasi (M)', format = "%.4f", step=0.0001, key = "H4")
        st.write("Konsentrasi = ", konsentrasi)
        
        # Tombol hitung
        if st.button ("Hitung pH", key = "B4"):
            OH_minus, pOH, pH = perhitungan_pH_basa_lemah(konsentrasi, konstanta_basa)
            st.write("[OH-] =", round(OH_minus, 4))
            st.write("pOH =", round(pOH, 2))
            st.write("pH =", round(pH, 2))
            st.success(f'pH basa adalah {pH:.2f}')


elif choice == "Massa dan Volume Asam":
    st.subheader("Menghitung [H+] dan pH dari Massa dan Volume Asam Kuat dan Asam Lemah")

    tab1, tab2 = st.tabs(["Asam Kuat", "Asam Lemah"])

    with tab1:
        st.subheader("Asam Kuat")
        
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
        st.subheader("Asam Lemah")
        
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
        konstanta_asam = st.number_input('Masukkan Ka', key = "K6")
        st.write("Ka = ", konstanta_asam)
        
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
            H_plus, pH = perhitungan_pH_asam_lemah_dengan_massa_volume_BM(massa, volume_dalam_liter, BM, konstanta_asam)
            st.write("[H+] =", round(H_plus, 4))
            st.write("pH =", round(pH, 2))
            st.success(f'pH asam adalah {pH:.2f}')

elif choice == "Massa dan Volume Basa":
    st.subheader(
        "Menghitung [OH-], pOH, dan pH dari Massa dan Volume Basa Kuat dan Basa Lemah")

    tab1, tab2 = st.tabs(["Basa Kuat", "Basa Lemah"])

    with tab1:
        st.subheader("Basa Kuat")

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
        st.subheader("Basa Lemah")

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
        konstanta_basa = st.number_input('Masukkan Kb', key = "K8")
        st.write("Kb = ", konstanta_basa)
        
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
                massa, volume_dalam_liter, BM, konstanta_basa)
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
    st.write('Skala pH adalah skala logaritmik yang digunakan untuk menentukan keasaman atau kebasaan (alkalinitas) suatu larutan berair. Skalanya berkisar dari 0 hingga 14.')
    st.write('''
- Larutan asam memiliki pH kurang dari 7. Semakin rendah pH, ​​semakin asam larutan tersebut. 
- Larutan basa atau basa memiliki pH lebih besar dari 7. Semakin tinggi pH, semakin basa larutan tersebut. 
- PH 7 dianggap netral, artinya tidak bersifat asam atau basa. Air murni biasanya dianggap netral, dengan pH 7. 
''')
    st.write('Asam meningkatkan konsentrasi ion hidrogen (H+) dalam larutan, sedangkan basa menurunkannya dengan menghasilkan ion hidroksida (OH−) yang bergabung dengan ion hidrogen menghasilkan air.')
    
    st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fid%2Fvektor%2Fskala-ph-ph-indikator-universal-strip-uji-gm954645674-260647627&psig=AOvVaw1kl1bznlexd8KBKTlNi_xN&ust=1715487167170000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCIj8zJTehIYDFQAAAAAdAAAAABAE")

    #Rumus pH
    st.subheader("Rumus pH")
    
    st.write('pH Asam Kuat')
    latex_H_plus_kuat = "[H+] = Ma * a"
    st.write(f"${latex_H_plus_kuat}$")
    latex_pH_asam = "pH = -log [H+]"
    st.write(f"${latex_pH_asam}$")

    
    st.write('pH Asam Lemah')
    latex_H_plus_lemah = "[H+] = √(Ma * Ka)"
    st.write(f"${latex_H_plus_lemah}$")
    st.write(f"${latex_pH_asam}$")

    
    st.write('pH Basa Kuat')
    latex_OH_plus_kuat = "[OH-] = Mb * b"
    st.write(f"${latex_OH_plus_kuat}$")
    latex_pOH = "pOH = -log [OH-]"
    st.write(f"${latex_pOH}$")
    latex_pH = "pH = 14-pOH"
    st.write(f"${latex_pH}$")

    
    st.write('pH Basa Lemah')
    latex_OH_plus_lemah = "[OH-] = √Mb * Kb"
    st.write(f"${latex_OH_plus_lemah}$")
    st.write(f"${latex_pOH}$")
    st.write(f"${latex_pH}$")
    

    #Cara Menggunakan Kalkulator pH
    st.subheader("Cara Menggunakan Kalkulator pH")
    st.write('''Dari konsentrasi asam kuat :
1. Anda diberikan daftar beberapa senyawa asam kuat umum. Silakan pilih salah satunya.
2. Selanjutnya, masukkan konsentrasi dalam satuan molar (M).
3. Klik Hitung pH, alat ini akan segera menentukan [H+] dan pH dari ion Hidrogen.

Dari konsentrasi asam lemah :
1. Anda diminta untuk memasukkan nilai konstanta asam (Ka).
2. Selanjutnya, masukkan konsentrasi dalam satuan molar (M).
3. Klik Hitung pH, alat ini akan segera menentukan [H+] dan pH dari ion Hidrogen.

Dari konsentrasi basa kuat :
1. Anda diberikan daftar beberapa senyawa basa kuat umum. Silakan pilih salah satunya.
2. Selanjutnya, masukkan konsentrasi dalam satuan molar (M).
3. Klik Hitung pH, alat ini akan segera menentukan [OH-], pOH, dan pH dari ion Hidroksida.

Dari konsentrasi basa lemah :
1. Anda diminta untuk memasukkan nilai konstanta basa (Kb).
2. Selanjutnya, masukkan konsentrasi dalam satuan molar (M).
3. Klik Hitung pH, alat ini akan segera menentukan [OH-], pOH, dan pH dari ion Hidrogen.

Dari massa dan volume asam kuat :
1. Anda diberikan daftar beberapa senyawa asam kuat umum. Silakan pilih salah satunya.
2. Selanjutnya, masukkan massa dalam satuan gram (g) dan masukkan volume dalam satuan mililiter (mL).
3. Klik Hitung pH, alat ini akan segera menentukan [H+] dan pH dari ion Hidrogen.

Dari massa dan volume asam lemah :
1. Anda diberikan daftar beberapa senyawa asam lemah umum. Silakan pilih salah satunya.
2. Selanjutnya, masukkan nilai konstanta asam (Ka), masukkan massa dalam satuan gram (g) dan masukkan volume dalam satuan mililiter (mL).
3. Klik Hitung pH, alat ini akan segera menentukan [H+] dan pH dari ion Hidrogen.

Dari massa dan volume basa kuat :
1. Anda diberikan daftar beberapa senyawa basa kuat umum. Silakan pilih salah satunya.
2. Selanjutnya, masukkan massa dalam satuan gram (g) dan masukkan volume dalam satuan mililiter (mL).
3. Klik Hitung pH, alat ini akan segera menentukan [OH-], pOH, dan pH dari ion Hidrogen.

Dari massa dan volume basa lemah :
1. Anda diberikan daftar beberapa senyawa basa lemah umum. Silakan pilih salah satunya.
2. Selanjutnya, masukkan nilai konstanta basa (Kb), masukkan massa dalam satuan gram (g) dan masukkan volume dalam satuan mililiter (mL).
3. Klik Hitung pH, alat ini akan segera menentukan [OH-], pOH, dan pH dari ion Hidrogen.
''')
