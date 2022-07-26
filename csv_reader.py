import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.header('GPV VALVE TIMES READER')
gv=pd.DataFrame()
gv['G1']=0
uploaded_file = st.file_uploader("Upload csv file here:")
if uploaded_file is not None:
     df=pd.read_csv(uploaded_file,low_memory=False)
     for i in range(9,len(df),100):
          gv.loc[i,'G1']=df.iloc[len(df)-i,1]
     st.write(gv.loc[:,:])
     fig,ax = plt.subplots(figsize=[12,8])
     ax.plot(gv.loc[:,'G1'],label='GV1')
     ax.legend()
     ax.set_title('VALVE TIMES')
     #ax.set_xlabel('x label')
     ax.set_ylabel('Travel')
     #ax.grid(True)
     st.pyplot(fig)
