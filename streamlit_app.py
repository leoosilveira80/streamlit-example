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
