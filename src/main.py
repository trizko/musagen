import streamlit as st

# Add a title
st.title("My First Streamlit App")

# Add some text
st.write("Hello, World!")

# Add an input field
name = st.text_input("What's your name?", "Type your name here...")

# Display the user's input
if name:
    st.write(f"Hello, {name}!")