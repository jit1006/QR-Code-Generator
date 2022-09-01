import streamlit as st
import qrcode 
from PIL import Image
import io
import os


# text= input("enter any test :")
st.title("Generate OR code in Fun :)")
title = st.text_input('Enter the txt :', ':)')    
st.write(requirements.txt)
if title is not None:
     
     img = qrcode.make(title)
     img.save("qrcode.jpg")
     st.image("qrcode.jpg" , caption='QR CODE IMAGE :) ')
     with open("qrcode.jpg", "rb") as file:
          st.title("Download the QR Image :)")
          btn = st.download_button(
               label="Download",
               data=file,
               file_name="oqcode.jpg",
               mime="image/png"
               
               )
     
else:
     st.image("qrcode1.png", caption='QR CODE IMAGE :) ')
     with open("qrcode1.png", "rb") as file:
          st.title("Download the QR Image :)")
          btn = st.download_button(
               label="Download",
               data=file,
               file_name="oqcode.jpg",
               mime="image/png"
               
               )
          
               
     
     
# img = qrcode.make(title)
# img.save("qrcode1.jpg")



