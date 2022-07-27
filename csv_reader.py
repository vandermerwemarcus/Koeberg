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
          gv.loc[i,'G1']=float(df.iloc[i,1])
     #st.write(gv.loc[:,:])
     
     fig,ax = plt.subplots(figsize=[12,6])
     ax.plot(gv.loc[10:,'G1'],label='GV1')
     ax.legend()
     ax.set_title('VALVE TIMES')
     ax.set_yticks([0,5,10])
     #ax.set_xticks([0,5,10])
     ax.set_yticklabels(['2','4','6','8','10'])
     ax.set_xticklabels(['','0','20','40','60','80','100'])
     ax.set_ylabel('Travel')
     ax.set_xlabel('x label')
     ax.grid(True)
     st.pyplot(fig)

