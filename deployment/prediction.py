import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Library Random Data
from scipy.stats import randint

from datetime import datetime, timedelta
from sklearn.utils import shuffle

def model_page():
    st.title("Model Prediction of Credit Card Fault")
    st.write("The model predicts whether the customer's transaction is fraud or not")
    st.sidebar.header('User Input Features')

    input_data = user_input()

    st.subheader('User Input')
    st.write(input_data)

    # Load the model using a context manager to ensure the file is closed
    with open("XGB_best_model.pkl", "rb") as f:
        load_model = joblib.load(f)

    prediction = load_model.predict(input_data)

    if prediction == 1:
        prediction = 'The Transaction is Fraud'
    else:
        prediction = 'The Transaction is Legit'

    st.write('Based on user input, the model predicted: ')
    st.write(prediction)

def user_input(num_rows=1):
    data = generate_data(num_rows)
    return data

def generate_data(num_rows=555719):
    trans_date_trans_time = st.sidebar.date_input("Transaction Date", value=datetime.now(), min_value=datetime.now() - timedelta(days=365), max_value=datetime.now())
    trans_date_trans_time = [trans_date_trans_time for _ in range(num_rows)]

    cc_num = st.sidebar.number_input("Credit Card Number", value=500000, min_value=100000, max_value=999999)
    cc_num = [cc_num for _ in range(num_rows)]

    merchant = st.sidebar.selectbox("Merchant", ['Merchant1', 'Merchant2', 'Merchant3'])
    merchant = [merchant for _ in range(num_rows)]

    category = st.sidebar.selectbox("Category", ['Personal', 'Childcare', 'Food', 'Transportation'])
    category = [category for _ in range(num_rows)]

    amt = st.sidebar.number_input("Amount", value=500, min_value=0, max_value=100000)
    amt = [amt for _ in range(num_rows)]

    first = st.sidebar.text_input("First Name")
    first = [first for _ in range(num_rows)]

    last = st.sidebar.text_input("Last Name")
    last = [last for _ in range(num_rows)]

    gender = st.sidebar.selectbox("Gender", ['Male', 'Female'])
    gender = [gender for _ in range(num_rows)]

    street = st.sidebar.text_input("Street")
    street = [street for _ in range(num_rows)]

    city = st.sidebar.text_input("City")
    city = [city for _ in range(num_rows)]

    state = st.sidebar.selectbox("State", ['NY', 'CA', 'IL', 'TX'])
    state = [state for _ in range(num_rows)]

    zip_code = st.sidebar.text_input("Zip Code")
    zip_code = [zip_code for _ in range(num_rows)]

    lat = st.sidebar.number_input("Latitude", value=40.7128, min_value=-90., max_value=90.)
    lat = [lat for _ in range(num_rows)]

    long_ = st.sidebar.number_input("Longitude", value=-74.0060, min_value=-180., max_value=180.)
    long_ = [long_ for _ in range(num_rows)]

    city_pop = st.sidebar.number_input("City Population", value=10000, min_value=10000, max_value=1000000)
    city_pop = [city_pop for _ in range(num_rows)]

    job = st.sidebar.selectbox("Job", ['Software Engineer', 'Doctor', 'Lawyer', 'Teacher'])
    job = [job for _ in range(num_rows)]

    dob = st.sidebar.date_input("Date of Birth", value=datetime.now() - timedelta(days=365*70), min_value=datetime.now() - timedelta(days=365*100), max_value=datetime.now())
    dob = [dob for _ in range(num_rows)]

    trans_num = np.arange(1, num_rows + 1)

    unix_time = st.sidebar.number_input("Unix Time", value=int(datetime.now().timestamp()), min_value=0, max_value=int(datetime.now().timestamp()))
    unix_time = [unix_time for _ in range(num_rows)]

    merch_lat = st.sidebar.number_input("Merchant Latitude", value=40.7128, min_value=-90., max_value=90.)
    merch_lat = [merch_lat for _ in range(num_rows)]

    merch_long = st.sidebar.number_input("Merchant Longitude", value=-74.0060, min_value=-180., max_value=180.)
    merch_long = [merch_long for _ in range(num_rows)]

    age = st.sidebar.number_input("Age", value=30, min_value=18, max_value=80)
    age = [age for _ in range(num_rows)]

    

    data = {
        'Trans_date_trans_time': trans_date_trans_time,
        'Cc_num': cc_num,
        'Merchant': merchant,
        'Category': category,
        'Amt': amt,
        'First': first,
        'Last': last,
        'Gender': gender,
        'Street': street,
        'City': city,
        'State': state,
        'Zip': zip_code,
        'Lat': lat,
        'Long': long_,
        'City_pop': city_pop,
        'Job': job,
        'Dob': dob,
        'Trans_num': trans_num,
        'Unix_time': unix_time,
        'Merch_lat': merch_lat,
        'Merch_long': merch_long,
        'age': age,
        'category': category,
        'amt': amt,
        'state': state,
        'job': job
    }

    # Create a Pandas DataFrame
    df = pd.DataFrame(data)

    return df

# def main():
#     st.title("Credit Card Transaction Data")
#     st.write("This app generates random credit card transaction data.")

#     num_rows = st.slider("Number of rows", 100, 100000, 555719)

#     df = generate_data(num_rows)

#     st.write(df)

# if __name__ == "__main__":
#     main()