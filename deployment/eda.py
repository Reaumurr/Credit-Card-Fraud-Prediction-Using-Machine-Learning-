import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#Load data
fraud = pd.read_csv('fraud_test.csv')

# Define the percentage of data you want to sample
sample_percentage = 50  # Adjust this percentage as needed

# Randomly sample the data based on the percentage
data = fraud.sample(frac=sample_percentage/100, random_state=22)

# def annotate_bar(ax, custom_y_func, font_size=14):

#     for p in ax.patches:
#         # Calculate annotation
#         value = str(round(p.get_height(), 1))
#         x = (p.get_x() + p.get_width() / 2) * 0.99
#         y = ((p.get_y() + p.get_height() / 2) * 0.99)
        
#         y = custom_y_func(y)
#         ax.annotate(
#             value,
#             (x, y),
#             color="black",
#             size=font_size, ha='center', va='center'
#         )

def eda_page():

    st.title("Eksploratory Data Analysis")
    st.write('Analyze the DataFrame for Better Understanding')
    st.markdown("<h2><b>Top 10 Transaction Amount</b></h2>", unsafe_allow_html=True)

    # TOP Transaction Amount
    columns = ['job', 'state', 'city', 'merchant']
    fraud_labels = ['Not Fraud', 'Fraud']

    for col in columns:
        st.subheader(f"Top 10 transaction amount by {col}")
        fig, ax = plt.subplots(1, 2, figsize=(30, 5))
        for i, fraud_label in enumerate(fraud_labels):
            temp_data = data[data['is_fraud'] == (0 if fraud_label == 'Not Fraud' else 1)]
            top = temp_data.groupby(col)['amt'].sum().nlargest(10)
            ax[i].bar(top.index, top.values, color='#a1c9f4')
            ax[i].set_title(fraud_label)
            ax[i].set_xlabel(col)
            ax[i].set_ylabel('Amount')
            if col == 'state':
                ax[i].tick_params(axis='x', rotation=0)
            else:
                ax[i].tick_params(axis='x', rotation=90)
        st.pyplot(fig)
    st.write("**Explanation**:")
    markdown_text = """
    * From the top 10 transaction amount by job we can see `Science Writer` have the most fraud with over 10.000 transaction amount meanwhile `Film/Video editor` are the most non fraud with almost 160.000 transaction
    * From the top 10 transaction amount by state we can see `NY` have the most fraud with almost 60.000 transaction amount meanwhile `TX`are the most non fraud with above 1.400.000 transaction
    * From the top 10 transaction amount by city we can see `Camden` have the most fraud with over 10.000 transaction amount meanwhile `Meridian` are the most non fraud with almost 100.000 transaction
    * From the top 10 transaction amount by merchant we can see `Heathcote, Yost and Kertzmann` have most fraud with almost 10.000 transaction amount meanwhile `Killback-LLC` are the most non fraud with over 80.000 transaction
    """
    st.markdown(markdown_text)

    st.markdown("<h2><b>Top 10 Transaction Count</b></h2>", unsafe_allow_html=True)
    # By Transaction count
    columns = ['job', 'state', 'city', 'merchant']
    columns_name = ['Job', 'State', 'City', 'Merchant']
    fraud = ['Not Fraud', 'Fraud']

    for col, name in zip(columns, columns_name):
        st.subheader(f"Top 10 transaction by {name}")
        fig, ax = plt.subplots(1, 2, figsize=(30, 5))
        sns.set_palette("pastel")
        for i, fraud_label in enumerate(fraud):
            temp_data = data[data['is_fraud'] == (0 if fraud_label == 'Not Fraud' else 1)]
            top = temp_data.groupby(col).size().nlargest(10)
            ax[i].bar(top.index, top.values, color='#a1c9f4')
            ax[i].set_title(fraud_label)
            ax[i].set_xlabel(name)
            ax[i].set_ylabel('Count')
            if col == 'state':
                ax[i].tick_params(axis='x', rotation=0)
            else:
                ax[i].tick_params(axis='x', rotation=90)
        st.pyplot(fig)

    st.write("")  # Add a blank line

    st.write("**Explanation**:")
    markdown_text = """
    * From the top 10 transaction by job we can see `Color Technologist` have the most fraud with over 20 transaction meanwhile `Film/Video editor` are the most not fraud with over 2.000 transaction
    * From the top 10 transaction by state we can see `NY` have the most fraud with over 80 transaction meanwhile `TX`are the most not fraud with 20.000 transaction
    * From the top 10 transaction by city we can see `Camden` have the most fraud over 20 transaction meanwhile `Birmingham` are the most not fraud with almost 1.200 transaction
    * From the top 10 transaction by merchant we can see `Healthcore LLC.` have most fraud with 10 transaction meanwhile `Killback LLC.` are the most not fraud with almost 1.000 transaction
    """
    st.markdown(markdown_text)

    st.markdown("<h2><b>Total Number and Amount for Fraud and Non Fraud Transaction</b></h2>", unsafe_allow_html=True)
    
    def annotate_bar(ax, custom_y_func, font_size=14):
        for p in ax.patches:
            value = str(round(p.get_height(), 1))
            x = (p.get_x() + p.get_width() / 2) * 0.99
            y = ((p.get_y() + p.get_height() / 2) * 0.99)
            y = custom_y_func(y)
            ax.annotate(value, (x, y), color="black", size=font_size, ha='center', va='center')

    # Fraud and Not Fraud Transactions
    st.header("Fraud and Not Fraud Transactions Count")
    data_fraud_count = data['is_fraud'].apply(lambda x: "Fraud" if x == 1 else 'Not Fraud').value_counts().reset_index()
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.barplot(data=data_fraud_count, x='is_fraud', y='count', color='#c6def8', ax=ax)
    annotate_bar(ax, lambda y: 15000 if y < 10000 else y, font_size=14)
    ax.set_title("Total number of transaction for fraud and not fraud transaction", fontsize=12, fontweight='bold')
    ax.set_ylabel("Transaction count")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    st.pyplot(fig)

    # Fraud and Not Fraud Amount
    st.header("Fraud and Not Fraud Transactions Amount")
    data_fraud_amount = data.groupby('is_fraud')['amt'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.barplot(data=data_fraud_amount, x='is_fraud', y='amt', color='#c6def8', ax=ax)
    annotate_bar(ax, lambda y: 1900000 if y < 1200000 else y, font_size=12)
    ax.set_title("Total transaction amount for fraud and not fraud transaction", fontsize=12, fontweight='bold')
    ax.set_ylabel("Transaction amount")
    ax.set_xticklabels(['Not Fraud', 'Fraud'], rotation=0)
    st.pyplot(fig)

    st.write("**Explanation**:")
    markdown_text = """
    Based on visualisation above:
    * There is 276743 total number of transaction `not fraud` and 1117 `fraud` transaction
    * There is 18745296.5 total transaction amount of `not fraud` and 1117 `fraud` transaction
    """
    st.markdown(markdown_text)

    # Calculate age
    data['dob'] = pd.to_datetime(data['dob'])
    data['age'] = (2020 - data['dob'].dt.year)

    def apply_age_group(age):
        if age <= 18:
            return 'Teenager'
        elif age <= 25:
            return "Young Adult"
        elif age <= 64:
            return "Adult"
        else:
            return "Elder"

    data['age_group'] = data['age'].apply(apply_age_group)

    # Overview of dataset by month, gender, and category
    st.header("Overview of dataset by Age, gender, and category")
    columns = ['gender', 'category', 'age', 'age_group']
    columns_name = ['gender', 'category', 'age', 'age group']
    name = ['Not Fraud', 'Fraud']

    for col in columns:
        st.subheader("Distribution of transaction by " + columns_name[columns.index(col)])
        fig, ax = plt.subplots(1, 2, figsize=(15, 5))  # Create a subplot with 2 columns
        for i in range(0, 2):
            data_1 = data[data['is_fraud'] == i]
            if col == 'gender':
                ax[i].pie(data_1[col].value_counts(), labels=['Female', 'Male'], autopct='%1.1f%%')
            elif col == 'age_group':
                ax[i].pie(data_1[col].value_counts(), labels=data_1[col].value_counts().index, autopct='%1.1f%%')
            elif col == 'category':
                sns.countplot(data=data_1, y=col, order=data_1[col].value_counts().index, ax=ax[i])
            else:
                sns.histplot(data=data_1, x=col, ax=ax[i])
            ax[i].set_title(name[i])
            ax[i].set_xlabel(columns_name[columns.index(col)])
            if col == 'category':
                ax[i].set_xticklabels(ax[i].get_xticklabels(), rotation=90)
        st.pyplot(fig)

    st.write("**Explanation**:")
    markdown_text = """
    Based on visualisation above we can see:
    - There is 54,8% transaction of `female` and 45,2% transaction of `male` in `not fraud` and `fraud`
    - Most distribution of `not fraud` transaction by category is from `gas_transport` meanwhile in fraud is from shopping_net
    - In distribution transaction by age mostly between 30-40 in `fraud` and between 45-50 for `not fraud`
    - By age group mostly `not fraud` transaction is from Adult with 73,9% and `fraud` also from Adult with 74,6%
    """
    st.markdown(markdown_text)