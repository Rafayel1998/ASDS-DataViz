import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Correlation",
    page_icon="🤝",
)

placement_df = pd.read_csv("../Placement_Data_Full_Class.csv")
placement_df.drop(columns="sl_no", inplace=True)

placement_df["gender"] = placement_df["gender"].map(dict(F=0, M=1))
placement_df["workex"] = placement_df["workex"].map(dict(No=0, Yes=1))
placement_df["status"] = placement_df["status"].map({"Not Placed": 0, "Placed": 1})
placement_df_mini = placement_df.drop(
    columns=["ssc_b", "hsc_b", "hsc_s", "degree_t", "specialisation"]
)
columns = placement_df_mini.columns.tolist()
selected_col = st.multiselect("Select Grade", columns, default=columns)

fig = px.imshow(
    placement_df_mini[selected_col].corr().round(2),
    text_auto=True,
    color_continuous_scale='RdBu_r'
)
fig.update_layout(
    autosize=False,
    width=800,
    height=800,
)

st.plotly_chart(fig, use_container_width=True)
