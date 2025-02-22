import streamlit as st
import requests

def get_exchange_rate(target_currency):
    url = "https://api.exchangerate-api.com/v4/latest/PKR"
    response = requests.get(url)
    data = response.json()
    return data['rates'].get(target_currency, None)

# Streamlit App UI
st.title("PKR Currency Converter")
st.write("Convert Pakistani Rupees (PKR) into multiple currencies using real-time exchange rates.")

# User Inputs
target_currencies = st.multiselect("Select target currencies:", ["USD", "EUR", "GBP", "INR", "AUD", "CAD", "AED", "CNY", "TRY", "JPY"], default=["USD", "EUR", "GBP", "INR", "AUD"])
amount = st.number_input("Enter amount in PKR:", min_value=0.01, format="%.2f")

if st.button("CONVERT"):
    results = {}
    for currency in target_currencies:
        exchange_rate = get_exchange_rate(currency)
        if exchange_rate:
            converted_amount = amount * exchange_rate
            results[currency] = f"{converted_amount:.2f} {currency}"
        else:
            results[currency] = "Exchange rate not available"
    
    for currency, result in results.items():
        st.success(f"{amount} PKR is equal to {result}")
