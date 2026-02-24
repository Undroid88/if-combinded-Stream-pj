import streamlit as st
st.title("Welcome to my Quiz App")

user_input = st.text_input("Your Name")

if user_input:
    st.write(f"Hello, {user_input.title()}")

# To run the sample, run:
# streamlit run app_sample.py
