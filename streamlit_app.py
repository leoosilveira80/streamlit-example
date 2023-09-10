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

import streamlit as st
import cv2
import numpy as np

def compare_images(img1, img2):
    # Load the images
    img1 = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2, cv2.IMREAD_GRAYSCALE)

    # Calculate the absolute difference between the images
    diff = cv2.absdiff(img1, img2)

    # Threshold the difference image to highlight the differences
    _, diff = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Save the difference image
    cv2.imwrite("difference.tif", diff)

st.title("TIFF Image Comparison")

img1 = st.file_uploader("Upload File 1 (TIFF)", type=["tif"])
img2 = st.file_uploader("Upload File 2 (TIFF)", type=["tif"])

if img1 is not None and img2 is not None:
    compare_images(img1, img2)
    st.image("difference.tif", caption="Difference Image", use_column_width=True)
