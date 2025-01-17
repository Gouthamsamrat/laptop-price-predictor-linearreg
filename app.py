import streamlit as st
from joblib import load
import numpy as np
import pandas as pd

st.title("Laptop Price Predictor Tool")
col1, col2 = st.columns(2)
with col1:
    st.image('laptop.jpg')
with col2:
st.markdown(""" #### Enter Your Specifications"""
# Import the model
regressor = load('regressor.joblib')
df = load('data.joblib')

st.title("Laptop Price Predictor")

# Brand
company = st.selectbox('Brand', df['Company'].unique())

# Type of Laptop
type = st.selectbox('Type', df['TypeName'].unique())

# RAM
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 16, 24, 32, 64])

# Weight
weight = st.number_input("Weight of the Laptop (in kg)")

# Touchscreen
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

# IPS Display
ips = st.selectbox('IPS Display', ['No', 'Yes'])

# Screen Size
screen_size = st.number_input('Screen Size (in inches)')

# Resolution
resolution = st.selectbox('Screen Resolution', [
    '1920x1080', '1366x768', '1600x900',
    '3840x2160', '3200x1800', '2880x1880',
    '2560x1600', '2560x1440', '2304x1440'
])

# CPU
cpu = st.selectbox('CPU', df['Cpu brand'].unique())

# HDD
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])

# SSD
ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])

# GPU
gpu = st.selectbox('GPU', df['Gpu brand'].unique())

# OS
os = st.selectbox('OS', df['os'].unique())

# Button for prediction
if st.button('Predict Price'):
    # Process inputs
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size

    # Define query DataFrame with the correct column names
    columns = ['Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen',
               'Ips', 'ppi', 'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os']
    query = pd.DataFrame(
        data=[[company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os]],
        columns=columns
    )

    # Make prediction and display the result
    prediction = regressor.predict(query)[0]
    st.title(f'Predicted Price: ₹{int(prediction)}')
