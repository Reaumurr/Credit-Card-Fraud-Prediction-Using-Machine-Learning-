import streamlit as st
import numpy as np
import pandas as pd
import joblib

import eda
from eda import eda_page
import prediction
from prediction import model_page

#Load data
fraud = pd.read_csv('fraud_test.csv')

# Define the percentage of data you want to sample
sample_percentage = 50  # Adjust this percentage as needed

# Randomly sample the data based on the percentage
data = fraud.sample(frac=sample_percentage/100, random_state=22)  # Set a random seed for reproducibility

st.header('Milestone 2')
st.write("""
Created by Reski Hidayat - HCK015 """)

st.write("This program is made to predict Credit Card Fraud using Model Classification.")
st.write("Dataset `fraud_test`")
data

def main():
    # Define menu options
    menu_options = ["Data Analysis", "Model Prediction"]

    # Create sidebar menu
    selected_option = st.sidebar.radio("Menu", menu_options)

    # Display selected page
    if selected_option == "Data Analysis":
        eda_page()
    elif selected_option == "Model Prediction":
        model_page()


if __name__ == "__main__":
    main()