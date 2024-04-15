import streamlit as st

st.sidebar.radio('Choose:',[1,2])

st.title("Hello World")

st.markdown('_Markdown_')

st.header('My header')

# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")