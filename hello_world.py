# hello_world.py

import streamlit as st

# Add a header to the sidebar
st.sidebar.header('My sidebar')
st.sidebar.markdown('Some sidebar text will go here!')

# Set the title of the app
st.title('Title in main section')
st.subheader('And a subtitle')

st.write('Hi, David!')

user_input = st.text_input('Enter any number: ', key='user_input')

try:
    user_input = float(user_input)
    user_input_squared = user_input ** 2
    st.write(f'{user_input} squared is {user_input_squared}')
except ValueError:
    st.write('Please enter a valid number.')
    
st.write('---')
