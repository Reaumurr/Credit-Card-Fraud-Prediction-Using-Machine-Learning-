# Credit Card Fraud Prediction Using Machine Learning

This program is made to predict Credit Card Fraud using Model Classification.

Source taken from Kaggle.com with Dataset Title `Credit Card Fraud Prediction`
[Dataset](https://www.kaggle.com/datasets/kelvinkelue/credit-card-fraud-prediction/data)

This dataset offers a variety of attributes valuable for comprehensive analysis. It contains 555,719 instances and 22 attributes, a mix of categorical and numerical data types. Importantly, the dataset is complete with no null values. Here's a breakdown of the attributes:

| Feature | Description |
| :--- | :--- |
| Trans_date_trans_time | Timestamp of the transaction (date and time).|
| Cc_num | Unique customer identification number. |
| Merchant | The merchant involved in the transaction. |
| Category | Transaction type (e.g., personal, childcare). |
| Amt | Transaction amount. |
| First | Cardholder's first name. |
| Last | Cardholder's last name. |
| Gender | Cardholder's gender. |
| Street | Cardholder's street address. |
| City | Cardholder's city of residence. |
| State | Cardholder's state of residence. |
| Zip | Cardholder's zip code. |
| Lat | Latitude of cardholder's location. |
| Long | Longitude of cardholder's location. |
| City_pop | Population of the cardholder's city. |
| Job | Cardholder's job title. |
| Dob | Cardholder's date of birth. |
| Trans_num | Unique transaction identifier. |
| Unix_time | Transaction timestamp (Unix format). |
| Merch_lat | Merchant's location (latitude). |
| Merch_long | Merchant's location (longitude). |
| Is_fraud | Fraudulent transaction indicator (1 = fraud, 0 = legitimate). This is the target variable for classification purposes.|

# Model Result
The model was able to correctly identify **85.17%** of the actual positive instances.

# Business Insight

This model can be used to improve fraud detection and prevention efforts. By accurately identifying fraudulent transactions, businesses can take action to prevent further losses and protect their customers. Additionally, the model can be used to identify patterns and trends in fraudulent behavior, which can help businesses to develop more effective fraud prevention strategies.

Furthermore, the use of random data to generate predictions based on entered features suggests that the model is flexible and can be applied to a wide range of scenarios. This means that businesses can use the model to analyze data from different sources and make predictions about fraudulent behavior in real-time.

Overall, the XGBoost model provides a valuable tool for businesses to improve their fraud detection and prevention efforts, and can help to reduce losses and protect customers. By accurately identifying fraudulent transactions and identifying patterns in fraudulent behavior, businesses can take proactive steps to prevent fraud and improve their overall security posture.

# Deployment
The application is deployed on Hugging Face Spaces. Access it using the following link:
[Credit Card Fraud Detection on Hugging Face](https://huggingface.co/spaces/Reaumur/Credit-Card-Fraud-Detection)
