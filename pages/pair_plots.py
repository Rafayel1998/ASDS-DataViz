import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Pair plots",
    page_icon="👫",
)

placement_df = pd.read_csv("Placement_Data_Full_Class.csv")
placement_df.drop(columns="sl_no", inplace=True)

categorical_col = ["gender", "ssc_b", "hsc_b", "hsc_s", "degree_t", "workex", "specialisation", "status"]
numerical_col = placement_df.columns.difference(categorical_col).tolist()
selected_col = st.multiselect("Select Grade", numerical_col, default=numerical_col)

fig = px.scatter_matrix(
    placement_df,
    dimensions=selected_col,
    color="status",
    symbol="gender"
)
fig.update_layout(
    autosize=False,
    width=1600,
    height=900,
)
st.plotly_chart(fig, use_container_width=True)
