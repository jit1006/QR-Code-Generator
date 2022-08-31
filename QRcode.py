import streamlit as st
import qrcode 
import io
import os

# text= input("enter any test :")
txt = st.text_area('Text to analyze', '''
     It was the best of times, it was the worst of times, it was
     the age of wisdom, it was the age of foolishness, it was
     the epoch of belief, it was the epoch of incredulity, it
     was the season of Light, it was the season of Darkness, it
     was the spring of hope, it was the winter of despair, (...)
     ''')
st.write('Sentiment:', run_sentiment_analysis(txt))
# img = qrcode.make(txt)
# img.save("qrcode1.jpg")
