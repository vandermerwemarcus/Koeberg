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
     fig=plt.figure(figsize=(10,6),tight_layout=True,dpi=100)#, dpi=200) #Allows the figure size to be specified
     ax1=fig.add_subplot(3,1,1)
     plt.grid(which='both', axis='both')
     plt.yscale('log')
     ax2=fig.add_subplot(3,1,2,sharex=ax1) #sharex aligns the x-axis'
     plt.grid(which='both', axis='both')
     ax3=fig.add_subplot(3,1,3,sharex=ax1)
     plt.grid(which='both', axis='both')
     ax1.plot(df.iloc[9:100,1])
     #plt.yscale('log')
     ax2.plot(df.iloc[9:100,1])
     #ax3.plot(UZ.loc[:,'MACD'])
     ax1.set_title('Security')
     ax2.set_title('ROC=10-50')
     ax3.set_title('ROC=2-8')
     plt.show()
