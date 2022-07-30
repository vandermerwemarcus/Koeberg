import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
st.header('GPV VALVE TIMES READER')
gv=pd.DataFrame()
gv['G1']=0
#Upload csv data:
uploaded_file = st.file_uploader("Upload csv file here:")
if uploaded_file is not None:
     @st.cache(suppress_st_warning=True,allow_output_mutation=True)
     def upload():
          global df
          df=pd.read_csv(uploaded_file,low_memory=False)
          return df
     upload()
     blocksize=float(df.iloc[2,1])
     st.write('Sample Size:',blocksize)
     samplerate=float(df.iloc[6,1])
     st.write('Sample Rate:',samplerate*1000,'ms')
     length=blocksize*samplerate
     
     slen=round(length,0)
     st.write('Recording Length:',slen,'seconds')
     start=0
     end=0
     for i in range(10,len(df),10):
          gv.loc[i,'G1']=float(df.iloc[i,1])
          if gv.loc[i,'G1']<10 and start==0:
               start=i
          if gv.loc[i,'G1']<0.1 and end==0:
               end=i
     #st.write(gv.loc[:,:])
     closing=(end-start)*samplerate
     st.write('Closing time:',closing,'sec')
     
     offset=slen/5
     xaxis = np.linspace(-offset,length,7)
     saxis=np.round(xaxis,decimals=0)
     fig,ax = plt.subplots(figsize=[12,6])
     ax.plot(gv.loc[10:,'G1'],label=df.iloc[1,1])
     ax.legend()
     ax.set_title('VALVE TIMES')
     ax.set_yticks([0,2,4,6,8,10])
     ax.set_yticklabels(['0','20','40','60','80','100'])
     ax.set_xticklabels(saxis)#(['','0','40','80','120','160','200'])
     ax.set_ylabel('Travel (% Open)')
     ax.set_xlabel('Time (sec)')
     ax.grid(True)
     st.pyplot(fig)

