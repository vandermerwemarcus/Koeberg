import streamlit as st
import pandas as pd
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     bytes_data = uploaded_file.getvalue()
     #st.write(bytes_data)
     df=pd.read_csv(uploaded_file,low_memory=False)
     st.write(df)
     st.line_chart(df.iloc[9:,1],width=10, height=10)
