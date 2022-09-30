import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
from predictions import predict

file = open('categories.json')
data = json.load(file)

def decode_category(ele, data=data):
    return data[ele].values()


months = decode_category("MONTH_NAME")
days = decode_category("DAY_NAME")
carriers = decode_category("CARRIER_NAME")
departing_airports = decode_category("DEPARTING_AIRPORT")
previous_airports = decode_category("PREVIOUS_AIRPORT")


st.title('Predicting Flight Delays')
st.markdown('Model for predicting if a flight will be delayed or not.')
# "MONTH_NAME", "DAY_NAME", "CARRIER_NAME", "DEPARTING_AIRPORT", "PREVIOUS_AIRPORT"

st.header('Flight Features')
col1, col2, col3 = st.columns(3) #need to reset columns to accomodate five features
with col1:
    # st.text('Sepal characteristics')
    month = st.selectbox('Select month', months)
    # day = st.selectbox('Select day', days)
    # previous_airport = st.selectbox("Select previous_airport", previous_airports)
with col2:
    previous_airport = st.selectbox("Select previous_airport", previous_airports)
    day = st.selectbox('Select day', days)
with col3:
    # st.text('Pepal characteristics')
    carrier_name = st.selectbox('Select Airport Carrier', carriers)
    departing_airport = st.selectbox('Select departing airport', departing_airports) #need categories + code for category encoding
    # previous_airport = st.selectbox("Select previous_airport", previous_airports)

def uncover(column, value):
    for ele in data[column].items():
        if value == ele[1]:
            # print(ele[1], int(ele[0]))
            return int(ele[0])
            print(value, ele[0])

month = uncover("MONTH_NAME", month)
day = uncover("DAY_NAME", day)
carrier_name = uncover("CARRIER_NAME", carrier_name)
departing_airport = uncover("DEPARTING_AIRPORT", departing_airport)
previous_airport = uncover("PREVIOUS_AIRPORT", previous_airport)
# st.button('Predict type of Iris')
data = [month, day, carrier_name, departing_airport, previous_airport]
print(data)

if st.button('Predict flight delay'):
    result = predict(pd.DataFrame([data],columns=['MONTH_NAME', 'DAY_NAME', 'CARRIER_NAME', 'DEPARTING_AIRPORT', 'PREVIOUS_AIRPORT']))
    st.text(result)