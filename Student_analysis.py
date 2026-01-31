import pandas as pd
import streamlit as st

st.title("Student Performance Analysis")

df = pd.read_csv("data.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset Summary")
st.write(df.describe())

if st.button("Show Dataset"):
    st.dataframe(df)

min_score = st.slider("Select Minimum Scores", 0, 100, 45)
filtered_df = df[df["Scores"] >= min_score]
st.dataframe(filtered_df)

uploaded_file = st.file_uploader("Upload CSV File")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

st.bar_chart(df["Subject"].value_counts())
