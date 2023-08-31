import streamlit as st

# Page title
st.title('Simple Streamlit App')

# Input field for user name
user_name = st.text_input('Enter your name', 'Your Name')

# Display user input
st.write(f'Hello, {user_name}!')

# Slider for selecting a number
selected_number = st.slider('Select a number', 1, 100, 50)
st.write(f'You selected: {selected_number}')

# Button to do something
if st.button('Click me'):
    st.write('Button clicked!')

# Checkbox
if st.checkbox('Show details'):
    st.write('Some additional details here.')

# Selectbox
options = ['Option 1', 'Option 2', 'Option 3']
selected_option = st.selectbox('Select an option', options)
st.write(f'Selected option: {selected_option}')
