import streamlit as st
import pandas as pd

st.title(':blue[SISTEM PERIODIK UNSUR]')

#import module
from tabulate import tabulate

#assign data
simbol = [
           ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
]

#create header
golongan = ['IA', 'IIA', 'IIIB', 'IVB', 'VB', 'VIB', 'VIIB', 'VIIIB', 'VIIIB', 'IB', 'IB', 'IIB', 'IIIA', 'IVA', 'VA', 'VIA', 'VIIA', 'VIIIA']

# display table
print(tabulate(simbol, headers=golongan, tablefmt="grid"))
