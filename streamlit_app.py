import streamlit as st

st.button("Reset", label="click to show two lines of texts below", type="primary")
if st.button('Let us go'):
    st.write('Success!')
