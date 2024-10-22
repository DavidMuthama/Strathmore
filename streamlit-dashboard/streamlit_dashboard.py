import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.subplots as sp

# Load the dataset
@st.cache
def load_df():
    return pd.read_csv('streamlit-dashboard/dataset.csv') 

df = load_df()
df_grouped = df.groupby(['year', 'sex'])[['total_inactive_population', 'total_unemployed_population', 'total_employed_population','Basic_unemployment','Intermediate_unemployment','Advanced_unemployment']].sum().reset_index()
# Simple Streamlit app using Plotly
st.title("Streamlit Dashboard with Plotly")
st.write("This is a simple example dashboard with Plotly visualizations.")

fig1 = px.line(df_grouped, x="year", y="total_inactive_population", color="sex",color_discrete_map={'male':'blue', 'female':'pink'}, title="Total Inactive Population By Sex")
st.plotly_chart(fig1)
fig2 = px.pie(df_grouped, values='total_inactive_population', names='sex', color='sex',
             color_discrete_map={'male':'blue', 'female':'pink'}, title="Total Inactive Population By Sex")
st.plotly_chart(fig2)

fig3 = px.line(df_grouped, x="year", y="total_unemployed_population", color="sex", color_discrete_map={'male':'blue', 'female':'pink'}, title="Total Unemployed Population")
st.plotly_chart(fig3)
fig4 = px.pie(df_grouped, values='total_unemployed_population', names='sex', color='sex',
             color_discrete_map={'male':'blue', 'female':'pink'}, title="Total Unemployed Population")
st.plotly_chart(fig4)

fig5 = px.line(df_grouped, x="year", y="total_employed_population", color="sex", color_discrete_map={'male':'blue', 'female':'pink'}, title="Total Employed Population")
st.plotly_chart(fig5)
fig6 = px.pie(df_grouped, values='total_employed_population', names='sex', color='sex',
             color_discrete_map={'male':'blue', 'female':'pink'}, title="Total Employed Population")
st.plotly_chart(fig6)


fig7 = px.pie(df_grouped, values='Basic_unemployment', names='sex', color='sex',
             color_discrete_map={'male':'blue', 'female':'pink'}, title="Employment status by basic education")
st.plotly_chart(fig7)