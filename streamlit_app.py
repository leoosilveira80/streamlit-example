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


import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Survey Results')
st.header('Survey Results 2021')
st.subheader('Was the tutorial helpful?')

### --- LOAD DATAFRAME
excel_file = 'Survey_Results.xlsx'
sheet_name = 'DATA'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='B:D',
                   header=3)

df_participants = pd.read_excel(excel_file,
                                sheet_name= sheet_name,
                                usecols='F:G',
                                header=3)
df_participants.dropna(inplace=True)

# --- STREAMLIT SELECTION
department = df['Department'].unique().tolist()
ages = df['Age'].unique().tolist()

age_selection = st.slider('Age:',
                        min_value= min(ages),
                        max_value= max(ages),
                        value=(min(ages),max(ages)))

department_selection = st.multiselect('Department:',
                                    department,
                                    default=department)

# --- FILTER DATAFRAME BASED ON SELECTION
mask = (df['Age'].between(*age_selection)) & (df['Department'].isin(department_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['Rating']).count()[['Age']]
df_grouped = df_grouped.rename(columns={'Age': 'Votes'})
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped,
                   x='Rating',
                   y='Votes',
                   text='Votes',
                   color_discrete_sequence = ['#F63366']*len(df_grouped),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)

# --- DISPLAY IMAGE & DATAFRAME
col1, col2 = st.columns(2)
image = Image.open('images/survey.jpg')
col1.image(image,
        caption='Designed by slidesgo / Freepik',
        use_column_width=True)
col2.dataframe(df[mask])

# --- PLOT PIE CHART
pie_chart = px.pie(df_participants,
                title='Total No. of Participants',
                values='Participants',
                names='Departments')

st.plotly_chart(pie_chart)

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
