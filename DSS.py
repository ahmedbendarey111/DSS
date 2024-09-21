from PIL import Image
import numpy as np
import pandas as pd #2
import streamlit as st

im = Image.open("DSS_Pic.png")
image= np.array(im)
st.image(image)
st.markdown(" <center>  <h1> Training Certificates Verification </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)
File="DSS.xlsx"
st.markdown(" <right>  <h1>Please Enter Serial Number </h1> </font> </right> </h1> ",
            unsafe_allow_html=True)
st.markdown(" <right>  <h1>                                     الرجاء إدخال كود الشهادة </h1> </font> </right> </h1> ",
            unsafe_allow_html=True)

SN = st.text_input("",value="",key="SN")


df = pd.read_excel(File,'Sheet1')
df.columns  = [i.replace(' ','_') for i in df.columns]
df.columns  = [i.upper() for i in df.columns]

#df['DATE']=df['DATE'].astype(str)
#df['DATE']=df['DATE'].str.split(' ').str[0]
#df['DATE']= pd.to_datetime(df['DATE'])
#df.dropna(axis=0, inplace=True)
df['CERTIFICATE_NO']=df['CERTIFICATE_NO'].astype('str')
Result=df[df['CERTIFICATE_NO']==SN]
Result=Result.T
df.fillna(0)
if st.button("Done"):
 st.dataframe(Result)


