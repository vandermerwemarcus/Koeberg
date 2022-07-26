import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title('GPV VALVE TIMES READER')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     df=pd.read_csv(uploaded_file,low_memory=False)
     
     fig,ax = plt.subplots(figsize=[12,8])
     y=df.iloc[9:,1]
     ax.plot(y,label='GV1')

     ax.legend()
     ax.set_title('VALVE TIMES')
     #ax.set_xlabel('x label')
     ax.set_ylabel('Travel')
     #ax.grid(True)
     st.pyplot(fig)
