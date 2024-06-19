import streamlit as st
import pickle

cv=pickle.load(open('cv.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

st.set_page_config("Language Detection")
st.header("Language detection")
input=st.text_input("Enter your text to detect language")
button=st.button("Detect Language")
if button:
    input=cv.transform([input])
    result=model.predict(input)
    st.subheader(result[0])
