import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
@st.cache
def load_data():
    return pd.read_csv('streamlit-dashboard/dataset.csv') 

data = load_data()

# Simple Streamlit app using Plotly
st.title("Streamlit Dashboard with Plotly")
st.write("This is a simple example dashboard with Plotly visualizations.")

d = {'value_options': ['male', 'female'], 'vote_flash_gordon': [3,6]}
df = pd.DataFrame(data=d)


pie_chart = px.pie(df,
                   title="film: PLACEHOLDER",
                   values="vote_flash_gordon",
                   names="value_options")

st.plotly_chart(pie_chart)

fig1 = px.line(data, x="year", y="population", color="sex", title="Population Over Time")
st.plotly_chart(fig1)
fig2 = px.pie(data,values='total_inactive_population',color="sex", title="Population Over Time")
st.plotly_chart(fig2)

fig3 = px.line(data, x="year", y="total_inactive_population", color="sex", title="Population Over Time")
st.plotly_chart(fig3)
fig4 = px.pie(data,values='total_inactive_population',color="sex", title="Population Over Time")
st.plotly_chart(fig4)

fig5 = px.line(data, x="year", y="total_unemployed_population", color="sex", title="Population Over Time")
st.plotly_chart(fig5)
fig6 = px.pie(data,color="sex", title="Population Over Time")
st.plotly_chart(fig6)

fig7 = px.line(data, x="year", y="total_employed_population", color="sex", title="Population Over Time")
st.plotly_chart(fig7)

fig8 = px.pie(data,color="sex", title="Population Over Time")
st.plotly_chart(fig8)