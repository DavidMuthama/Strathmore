import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
@st.cache
def load_df():
    return pd.read_csv('streamlit-dashboard/dataset.csv') 

df = load_df()

# Simple Streamlit app using Plotly
st.title("Streamlit Dashboard with Plotly")
st.write("This is a simple example dashboard with Plotly visualizations.")

fig1 = px.line(df, x="year", y="population", color="sex", title="Population Over Time")
st.plotly_chart(fig1)
fig2 = px.pie(df, values='total_inactive_population', names='sex', color='sex',
             color_discrete_map={'male':'blue', 'female':'pink'})
st.plotly_chart(fig2)

fig3 = px.line(df, x="year", y="total_inactive_population", color="sex", title="Population Over Time")
st.plotly_chart(fig3)
fig4 = px.pie(df,values='total_inactive_population',color="sex", title="Population Over Time")
st.plotly_chart(fig4)

fig5 = px.line(df, x="year", y="total_unemployed_population", color="sex", title="Population Over Time")
st.plotly_chart(fig5)
fig6 = px.pie(df,color="sex", title="Population Over Time")
st.plotly_chart(fig6)

fig7 = px.line(df, x="year", y="total_employed_population", color="sex", title="Population Over Time")
st.plotly_chart(fig7)

fig8 = px.pie(df,color="sex", title="Population Over Time")
st.plotly_chart(fig8)