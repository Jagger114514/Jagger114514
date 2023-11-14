import streamlit as st

title_one = st.text_input('Type here to show what you want to show')
title_two = st.text_input('Type here to show what you want to show')

if st.button("Just do it!", help="click to show two lines of texts below"):
    st.write('The current movie title is', title_one)

st.button("reset", help="click here to restart", type="primary")
