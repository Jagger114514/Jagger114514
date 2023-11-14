import streamlit as st

st.button("reset", help="click here to restart", type="primary")
if st.button("Let us go", help="click to show two lines of texts below"):
    st.write('Success!')
    
title = st.text_input('Type here to show what you want to show')
st.write('The current movie title is', title)
