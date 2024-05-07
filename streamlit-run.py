import streamlit as st
import pandas as pd
import joblib

# Load the saved Gradient Boosting model
model = joblib.load('gradient_boosting_model.pkl')

# Define the function to make predictions
def predict_sales(data):
    prediction = model.predict(data)
    return prediction

def main():
    st.title('Sales Prediction App')

    st.sidebar.header('Input Parameters')

    # Collect input from user
    year = st.sidebar.number_input('Year', value=2023)
    dollars = st.sidebar.number_input('Dollars', value=0)
    dollars_last_year = st.sidebar.number_input('Dollars Last Year', value=0)
    unit_sales_last_year = st.sidebar.number_input('Unit Sales Last Year', value=0)
    dollars_3_years_ago = st.sidebar.number_input('Dollars 3 Years Ago', value=0)
    unit_sales_3_years_ago = st.sidebar.number_input('Unit Sales 3 Years Ago', value=0)
    percent_change_dollars_1_year = st.sidebar.number_input('Percent Change Dollars 1 Year', value=0.0)
    percent_change_units_1_year = st.sidebar.number_input('Percent Change Units 1 Year', value=0.0)
    percent_change_dollars_3_years = st.sidebar.number_input('Percent Change Dollars 3 Years', value=0.0)
    percent_change_units_3_years = st.sidebar.number_input('Percent Change Units 3 Years', value=0.0)

    # Create a DataFrame from the user input
    input_data = pd.DataFrame({
        'Dollars': [dollars],
        'Dollars last year': [dollars_last_year],
        'Unit sales last year': [unit_sales_last_year],
        'Dollars 3 years ago': [dollars_3_years_ago],
        'Unit sales 3 years ago': [unit_sales_3_years_ago],
        'Percent change dollars 1 year': [percent_change_dollars_1_year],
        'Percent change units 1 year': [percent_change_units_1_year],
        'Percent change dollars 3 years': [percent_change_dollars_3_years],
        'Percent change units 3 years': [percent_change_units_3_years]
    })

    # Make prediction
    if st.button('Predict'):
        prediction = predict_sales(input_data)
        st.success(f'The predicted sales for {year} is {prediction[0]}.')

if __name__ == '__main__':
    main()
