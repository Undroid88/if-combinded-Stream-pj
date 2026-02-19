import streamlit as st
st.title("Welcome to my App")

user_input = st.text_input("Your Name")

if user_input:
    st.write(f"Hello, {user_input.title()}")


