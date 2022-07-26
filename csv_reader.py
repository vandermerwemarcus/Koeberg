import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title('GPV VALVE TIMES READER')
uploaded_file = st.file_uploader("Upload csv file here:")
if uploaded_file is not None:
     df=pd.read_csv(uploaded_file,low_memory=False)
     
     fig,ax = plt.subplots(figsize=[12,8])
     ax.plot(df.iloc[9:,1],label='GV1')
     ax.plot(df.iloc[9:,2],label='GV2')
     ax.legend()
     ax.set_title('VALVE TIMES')
     #ax.set_xlabel('x label')
     ax.set_ylabel('Travel')
     #ax.grid(True)
     st.pyplot(fig)
