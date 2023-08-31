import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_excel('sample_product_costs.xlsx')

# Page title
st.title('Product Cost Analysis Dashboard')

# Sidebar for selecting a product
selected_product = st.sidebar.selectbox('Select a Product', df['Product'].unique())

# Filter the data based on the selected product
filtered_df = df[df['Product'] == selected_product]

# Show data summary
st.write(f"## Data Summary for {selected_product}")
st.write(filtered_df)

# Show scatter plot
st.write(f"## Cost Analysis for {selected_product}")
scatter_fig = px.scatter(filtered_df, x='Month', y='Cost', color='Category', title=f'Cost Analysis for {selected_product}')
st.plotly_chart(scatter_fig)

# Show bar chart for cost percentage by category
st.write(f"## Cost Percentage by Category for {selected_product}")
total_cost_by_month = filtered_df.groupby(['Month'])['Cost'].sum().reset_index()
filtered_df = filtered_df.merge(total_cost_by_month, on='Month', suffixes=('', '_total'))
filtered_df['Cost_Percentage'] = (filtered_df['Cost'] / filtered_df['Cost_total']) * 100
bar_fig = px.bar(filtered_df, x='Month', y='Cost_Percentage', color='Category',
                 title=f'Cost Percentage by Category for {selected_product}', range_y=[0, 100])
st.plotly_chart(bar_fig)
