import streamlit as st

st.title("Welcome To Chetan world")
st.markdown("I love python")
st.header("Python Form")

name = st.text_input("Enter your name")
fname = st.text_input("Enter your father name:")
adr = st.text_input("enter your text: ")
classdata = st.selectbox("Enter your class:",(1,2,3,4,5,6,7,8,9,10,11,12))

button = st.button("Done")
if button :
    st.markdown(f"""
    Name : {name}   ,
       Father Name : {fname} ,
          Address : {adr} ,
              Class : {classdata}
  """)