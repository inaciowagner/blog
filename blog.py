import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

with open("blog.html", "r", encoding='utf-8') as f:
    html_string = f.read()

components.html(html_string, height=500)

#st.markdown(
 #   """
  #  <iframe src="blog.html" width="100%" height="100%"></iframe>
   # """,
    #unsafe_allow_html=True
#)