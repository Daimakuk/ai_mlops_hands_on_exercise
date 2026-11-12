
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Bike Sharing Analytics",
    page_icon="🚲",
    layout="wide"
)
st.title("Bike Sharing Analytics")

st.write(
    "Interactive exploration of daily bike rental demand."
)

df = pd.read_csv("datasets/day.csv")


st.subheader("Dataset Preview")
st.dataframe(df.head(10))


st.metric(
    "Total Observations",
    len(df)
)
