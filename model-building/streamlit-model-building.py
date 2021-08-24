import streamlit as st
import pandas as pd

# st.write()
st.title("SMART FARMER")

df = pd.read_csv("df_crops.csv")
st.line_chart(df)
