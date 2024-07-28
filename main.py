import streamlit as st

st.title("This is the first website :sparkling_heart:")

st.write("hello")

ten = st.text_input("nhap ten")

b = st.button("print")
if b:
  st.write("hello", ten)

st.progress(50)
