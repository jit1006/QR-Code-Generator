import streamlit as st
import qrcode 
import io
import os

text= input("enter any test :")
img = qrcode.make(text)
img.save("qrcode1.jpg")
