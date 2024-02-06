import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn

# Load CSS for background image
background_css = r'''
    <style>
        body {
            background-image: url("https://images.nationalgeographic.org/image/upload/t_edhub_resource_key_image/v1638892233/EducationHub/photos/crops-growing-in-thailand.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            width: 100vw;
            height: 100vh;
            margin: 0;
            padding: 0;
        }
    </style>
'''


# Inject CSS into Streamlit app
st.markdown(background_css, unsafe_allow_html=True)

st.title('Crop Recommendation System🌱')
st.header('Please fill the required details mentioned below:-')

labels = {
    'rice': 0, 'maize': 1, 'jute': 2, 'cotton': 3, 'coconut': 4, 'papaya': 5, 'orange': 6,
    'apple': 7, 'muskmelon': 8, 'watermelon': 9, 'grapes': 10, 'mango': 11,
    'banana': 12, 'pomegranate': 13, 'lentil': 14, 'blackgram': 15, 'mungbean': 16,
    'mothbeans': 17, 'pigeonpeas': 18, 'kidneybeans': 19, 'chickpea': 20, 'coffee': 21
}

# Load the model
model = pickle.load(open('rfc.pkl', 'rb'))

def recomm(N, P, K, Temp, Hum, ph, Rain):
    features = pd.DataFrame([[N, P, K, Temp, Hum, ph, Rain]],
                            columns=['N', 'P', 'K', 'Temperature', 'Humidity', 'ph', 'Rainfall'])
    rc_pred = model.predict(features)
    for key, value in labels.items():
        if value == rc_pred:
            return key

col1, col2, col3 = st.columns(3)

with col1:
    N = st.number_input('Enter the Nitrogen(N) levels in the soil:')
    Temp = st.number_input('Enter the Temperature in °C :')

with col2:
    P = st.number_input('Enter the Phosphorus(P) levels in the soil:')
    Hum = st.slider('Enter the Humidity in %', 0, 100, 50)

with col3:
    K = st.number_input('Enter the Potassium(K) levels in the soil:')
    ph = st.slider('Enter the pH level', 0, 14, 7)

Rain = st.number_input('Enter the Rainfall in mm:')

if st.button('GET RECOMMENDATION!'):
    a = recomm(N, P, K, Temp, Hum, ph, Rain)
    st.header(a)
