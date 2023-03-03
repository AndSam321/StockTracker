import streamlit as st
import pandas as pd

st.write("Window")

st.sidebar.write("Which dashboard")
option = st.sidebar.selectbox(
    'Which dashboard',
    ('Test', 'Test2'))
st.write("You selected", option)