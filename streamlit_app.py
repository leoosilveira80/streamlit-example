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
import pandas as pd
import plotly.express as px

# Set page title
st.title('Excel Data Analysis with Streamlit')

# Upload Excel file
uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])

if uploaded_file is not None:
    # Load Excel data
    df = pd.read_excel(uploaded_file)

    # Display data
    st.subheader('Data Preview')
    st.write(df)

    # Create a scatter plot
    st.subheader('Scatter Plot')
    scatter_fig = px.scatter(df, x='Month', y='Cost', color='Category', title='Cost Analysis')
    st.plotly_chart(scatter_fig)

    # Create a bar chart for cost percentage by category
    st.subheader('Cost Percentage by Category')
    total_cost_by_month = df.groupby(['Month'])['Cost'].sum().reset_index()
    df = df.merge(total_cost_by_month, on='Month', suffixes=('', '_total'))
    df['Cost_Percentage'] = (df['Cost'] / df['Cost_total']) * 100
    bar_fig = px.bar(df, x='Month', y='Cost_Percentage', color='Category',
                     title='Cost Percentage by Category', range_y=[0, 100])
    st.plotly_chart(bar_fig)

