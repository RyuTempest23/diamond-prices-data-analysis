# Importing the required libraries for this project
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Diamond Price Analysis", layout="wide")

st.title("💎 Diamond Price Analysis")

st.write(
    """
    A diamond is one of the most valuable stones in the world, and its
    price depends on far more than size alone. This app explores how
    carat, cut, color, and clarity interact to determine a diamond's price.
    """
)

st.image("diamond_no_bg.png", caption="A diamond")


# Load data — cache so the CSV isn't re-read on every interaction
@st.cache_data
def load_data():
    df = pd.read_csv("diamonds.csv")
    df = df.drop("Unnamed: 0", axis=1)
    return df


data = load_data()

st.subheader("Raw data (first 5 rows)")
st.dataframe(data.head())

st.subheader("Price vs Carat")
figure = px.scatter(
    data_frame=data,
    x="carat",
    y="price",
    size="depth",
    color="cut",
    trendline="ols",
)
st.plotly_chart(figure, use_container_width=True)
