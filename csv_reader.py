import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     #bytes_data = uploaded_file.getvalue()
     #st.write(bytes_data)
     df=pd.read_csv(uploaded_file,low_memory=False)
     st.write(df)
     #st.line_chart(df.iloc[9:100,1],width=10, height=10)
     
     fig,ax = plt.subplots(figsize=[10,5])
     y=df.iloc[9:100,1]
     ax.plot(y,label='GV1')

     ax.legend()
     ax.set_title('VALVE TIMES')
     #ax.set_xlabel('x label')
     ax.set_ylabel('Price')
     ax.grid(True)
     st.pyplot(fig)
