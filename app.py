import streamlit as st
import base64
import pandas as pd
import numpy as np
import pickle
import json
from predictions import predict
from PIL import Image

file = open('categories.json')
data = json.load(file)

def decode_category(ele, data=data):
    return data[ele].values()


months = decode_category("MONTH_NAME")
days = decode_category("DAY_NAME")
carriers = decode_category("CARRIER_NAME")
departing_airports = decode_category("DEPARTING_AIRPORT")
previous_airports = decode_category("PREVIOUS_AIRPORT")

img = Image.open("image.jpg")
new_image = img.resize((800, 200))
# st.image(new_image)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('flight.jpg') 


# st.image(img, use_column_width=True, width=10)


st.title('Predicting Flight Delays')
st.markdown('Model for predicting if a flight will be delayed or not.')
st.header('Flight Features')
col1, col2, col3 = st.columns(3) #need to reset columns to accomodate five features
with col1:
    month = st.selectbox('Select month', months)

with col2:
    previous_airport = st.selectbox("Select departing_airport", previous_airports) #previous_airports=departing airports
    day = st.selectbox('Select day', days)
with col3:
    carrier_name = st.selectbox('Select Airport Carrier', carriers)
    departing_airport = st.selectbox('Select destination airport', departing_airports) #destination airport = departing airports

def uncover(column, value):
    for ele in data[column].items():
        if value == ele[1]:
            return int(ele[0])
            # print(value, ele[0])

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