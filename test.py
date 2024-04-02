import streamlit as st
import pandas as pd

st.title(':blue[SISTEM PERIODIK UNSUR]')

st.write('Tabel periodik unsur dibawah ini:')
st.write(data_frame({
           'IA': ['H', 'Li', 'Na', 'K', 'Rb' ,'Cs' ,'Fr'],
}))
