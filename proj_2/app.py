import streamlit as st
st.title(":green[MOHAMMED ISMAIL] ")
st.snow()
st.header("Data science")
st.subheader("internship")

var='''print("Hello")'''
st.code(var,language="python")



btn_click=st.button("click")
if btn_click==True:
    st.subheader("You clicked me :cry:")
    st.balloons()