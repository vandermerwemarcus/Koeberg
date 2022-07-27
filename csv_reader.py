import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.header('GPV VALVE TIMES READER')
gv=pd.DataFrame()
gv['G1']=0
#Upload csv data:
uploaded_file = st.file_uploader("Upload csv file here:")
if uploaded_file is not None:
     df=pd.read_csv(uploaded_file,low_memory=False)
     for i in range(10,len(df),50):
          gv.loc[i,'G1']=df.iloc[i,1]
     st.write(gv.loc[:,:])
     
     #Plot data using Matplotlib:
     plt.plot(gv.loc[9:,'G1'])
     plt.show()

