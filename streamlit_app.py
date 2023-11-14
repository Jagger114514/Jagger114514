import streamlit as st

title = st.text_input('Type here to show what you want to show', key=1)

st.button("reset", help="click here to restart", type="primary")
if st.button("Just do it!", help="click to show two lines of texts below"):
    st.write('The current movie title is', title)
