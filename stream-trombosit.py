import pickle
import streamlit as st
import pandas as pd
import numpy as np
import math
import random

trombositmodel = pickle.load(open('trombositmodel.sav', 'rb'))

st.title('Prediksi Stadium Kanker Kolorektal')

age = st.text_input ('Age')

plt = st.text_input ('PLT')

pdw = st.text_input ('PDW')

mpv = st.text_input ('MPV')

pct = st.text_input('PCT')

tromb_diagnosis = ''

if st.button('Prediksi Stadium Kanker Kolorektal'):
    tromb_prediction = trombositmodel.predict([[age, plt, pdw, mpv, pct]])

    if(tromb_prediction[0] == 2):
        tromb_diagnosis = 'Stadium 2'
    if(tromb_prediction[0] == 3):
        tromb_diagnosis = 'Stadium 3'
    else:
        tromb_diagnosis = 'Stadium 4'
        
    st.success(tromb_diagnosis)
