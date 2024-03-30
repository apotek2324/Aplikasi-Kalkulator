import streamlit as st

st.header('_Aplikasi Penjumlahan Bilangan Numerik_', divider='blue')

angka_pertama = st.number_input('Masukkan angka pertama')
st.write('The first number is', angka_pertama)

angka_kedua = st.number_input('Masukkan angka kedua')
st.write('The second number is', angka_kedua)

operasi_matematika = angka_pertama * angka_kedua
st.write(f"Angka pertama {angka_pertama} x Angka kedua {angka_kedua} = {operasi_matematika}")