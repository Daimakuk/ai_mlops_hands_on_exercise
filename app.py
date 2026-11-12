
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Bike Sharing Analytics",
   
    layout="wide"
)

st.title("Bike Sharing Analytics")

st.write(
    "Interactive analysis of daily bike rental demand."
)

df = pd.read_csv("datasets/day.csv")


st.sidebar.header("Filters")

selected_year = st.sidebar.selectbox(
    "Select Year",
    ["All", "2011", "2012"]
)

if selected_year == "2011":
    filtered_df = df[df["yr"] == 0]

elif selected_year == "2012":
    filtered_df = df[df["yr"] == 1]

else:
    filtered_df = df

total_days = len(filtered_df)
total_rentals = filtered_df["cnt"].sum()
average_rentals = filtered_df["cnt"].mean()

st.subheader("Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Days Analyzed",
        total_days
    )

with col2:
    st.metric(
        "Total Rentals",
        f"{total_rentals:,}"
    )

with col3:
    st.metric(
        "Average Daily Rentals",
        f"{average_rentals:,.0f}"
    )


st.subheader("Dataset Preview")

st.dataframe(
    filtered_df,
    width="stretch",
    height=500,
    hide_index=True
)



st.subheader("Monthly Rental Trends")

monthly_rentals = (
    filtered_df
    .groupby("mnth")["cnt"]
    .mean()
)

st.line_chart(monthly_rentals)


st.subheader("Temperature vs Daily Rentals")

st.scatter_chart(
    filtered_df,
    x="temp",
    y="cnt"
)


correlation = filtered_df["temp"].corr(
    filtered_df["cnt"]
)

st.write(
    f"Temperature-rentals correlation: {correlation:.3f}"
)

# Compare registered and casual users
st.subheader("Casual vs Registered Users")

monthly_users = (
    filtered_df
    .groupby("mnth")[["casual", "registered"]]
    .mean()
)

st.bar_chart(monthly_users)
