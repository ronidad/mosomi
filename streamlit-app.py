import streamlit as st
import pandas as pd

st.write(" " "
#My app
Hello world
"
"
"
)

df= pd.read_csv("df_crops.csv")
st.line_chart(df)