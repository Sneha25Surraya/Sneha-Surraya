import streamlit as st

# Streamlit App UI
st.set_page_config(page_title="DMAS Calculator", page_icon="➕", layout="wide")

# Amazon-like Header
st.markdown(
    """
    <style>
        .header {
            background-color: #232f3e;
            padding: 10px 20px;
            color: white;
            font-size: 20px;
            font-weight: bold;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .header .logo {
            font-size: 24px;
            color: #ff9900;
        }
        .header .nav-links {
            display: flex;
            gap: 15px;
        }
        .header a {
            color: white;
            text-decoration: none;
            font-size: 16px;
        }
        .header a:hover {
            text-decoration: underline;
        }
    </style>
    <div class="header">
        <div class="logo">🛒 MyShop</div>
        <div class="nav-links">
            <a href="#">Home</a>
            <a href="#">Products</a>
            <a href="#">Deals</a>
            <a href="#">Cart</a>
            <a href="#">Profile</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

import streamlit as st
from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Streamlit App UI
st.title("Age Calculator App")
st.write("Enter your Date of Birth to calculate your age.")

# User Input for Date of Birth
dob = st.date_input("Select your Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())

if st.button("Calculate Age"):
    age = calculate_age(dob)
    st.success(f"You are {age} years old!")