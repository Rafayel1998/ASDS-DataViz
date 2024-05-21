import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Grades",
    page_icon="💯",
)

placement_df = pd.read_csv("Placement_Data_Full_Class.csv")
placement_df.drop(columns="sl_no", inplace=True)

grades = ["degree_p", "etest_p", "hsc_p", "mba_p", "ssc_p"]
selected_grade = st.selectbox("Select Grade", grades)

fig = px.violin(placement_df, y=selected_grade)

st.plotly_chart(fig, use_container_width=True)
