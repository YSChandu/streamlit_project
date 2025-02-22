import streamlit as st

st.title("Hello, Boss! 🚀")  # Title
st.header("This is a header")     # Header
st.subheader("This is a subheader") # Subheader
st.write("This is some normal text.") # Normal text

name = st.text_input("Enter your name") # Input box
if st.button("Greet"):
    st.write(f"Hello, {name}! 😊") # Display output
