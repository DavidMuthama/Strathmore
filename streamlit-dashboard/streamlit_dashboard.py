import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.subplots as sp

# Load the dataset
@st.cache
def load_df():
    return pd.read_csv('streamlit-dashboard/dataset.csv') 

df = load_df()

# Simple Streamlit app using Plotly
st.title("Streamlit Dashboard with Plotly")
st.write("This is a simple example dashboard with Plotly visualizations.")

fig1 = px.line(df, x="year", y="total_inactive_population", color="sex",color_discrete_map={'male':'blue', 'female':'pink'}, title="Total Inactive Population By Sex")
# st.plotly_chart(fig1)
fig2 = px.pie(df, values='total_inactive_population', names='sex', color='sex',
             color_discrete_map={'male':'blue', 'female':'pink'}, title="Total Inactive Population By Sex")
# st.plotly_chart(fig2)

fig3 = px.line(df, x="year", y="total_unemployed_population", color="sex", color_discrete_map={'male':'blue', 'female':'pink'}, title="Total Unemployed Population")
# st.plotly_chart(fig3)
fig4 = px.pie(df, values='total_unemployed_population', names='sex', color='sex',
             color_discrete_map={'male':'blue', 'female':'pink'}, title="Total Unemployed Population")
# st.plotly_chart(fig4)

fig5 = px.line(df, x="year", y="total_employed_population", color="sex", color_discrete_map={'male':'blue', 'female':'pink'}, title="Total Employed Population")
# st.plotly_chart(fig5)
fig6 = px.pie(df, values='total_employed_population', names='sex', color='sex',
             color_discrete_map={'male':'blue', 'female':'pink'}, title="Total Employed Population")
# st.plotly_chart(fig6)

# Create subplots with shared x-axes
fig = sp.make_subplots(rows=2, cols=1, shared_xaxes=True)

# Add the first three figures to the top subplot
fig.add_trace(fig1.data[0], row=1, col=1)
fig.add_trace(fig3.data[0], row=1, col=1)
fig.add_trace(fig5.data[0], row=1, col=1)

# Add the last three figures to the bottom subplot
fig.add_trace(fig2.data[0], row=2, col=1)
fig.add_trace(fig4.data[0], row=2, col=1)
fig.add_trace(fig6.data[0], row=2, col=1)

# Update the layout
fig.update_layout(height=600)
st.plotly_chart(fig)