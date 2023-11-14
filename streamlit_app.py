import streamlit as st

st.button("Let us go", type="primary")
if st.button("Let us go", help="click to show two lines of texts below", ):
    st.write('Success!')
