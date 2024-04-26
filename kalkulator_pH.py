st.header('KALKULATOR pH', divider='blue')

senyawa_asam_kuat = st.selectbox(
    "Masukkan senyawa asam",
    ("Asam Nitrat-HNO3","Asam Klorida-HCl","Asam Sulfat-H2SO4","Asam Iodida-HI","Asam Flourida-HF"))

senyawa_basa_kuat = st.selectbox(
    "Masukkan senyawa basa"
    ("Kalium Hidroksida-KOH","Natrium Hidroksida-NaOH","Litium Hidroksida-LiOH","Kalsium Hidroksida-Ca(OH)2"))

st.write('Anda memilih:', option)