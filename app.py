import streamlit  as st
import pandas as pd
import numpy as np

st.title("Hello , Streamlit ")
st.write("this is your 1st streamlit :streamlit:")
st.text("let's get started")
name=st.text_input("Enter your name:")

if(st.button("Greets!")):
    st.success(f"Hello {name} ma'am!")
df = pd.DataFrame(np.random.randn(10,2),columns=['A','B'])
st.line_chart(df) 
st.bar_chart(df)
st.video("https://youtu.be/jhBAUzoXj_A?si=UCopHkXkIEbifI0b")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOzyFEYqkfqQndmgOzZOOARlzz0aG-awZi9pckun0Qeg&s=10")
upload_file=st.file_uploader("upload a csv.",type="csv")
if upload_file:
    df=pd.read_csv(upload_file)
    st.dataframe(df)
st.sidebar.title("Navigator")
st.number_input("Enter your marks",min_value=0,max_value=100)
st.slider("Give rating ",0,10)
st.text_area("Enter 300s word essay:")
st.markdown("I am **bold**, I am *italic*, I am `code`, [YCCE](https://ycce.edu/)")
st.code("for i in range(5):print(i)",language="python")
st.selectbox("select your grade",["A","B","C"])
st.multiselect("select your choice",["chutti","roj chutti","roj ghr me rho"])
st.radio("select",["yes","no"])
st.checkbox("Agree to T&C")
option=st.radio("select your preference",["A","B","C"])
if option=="A":
  st.write("enjoy holiday")
if option=="B":
   st.write("no holiday")
if option=="C":
   st.write("come to class")