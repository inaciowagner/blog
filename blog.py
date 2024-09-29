import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# cabeçalho do blog
st.html("<img src='https://raw.githubusercontent.com/inaciowagner/blog/refs/heads/main/casa_do_carvalho.png'>")
st.html("<hr/>")


# arquivo
with open("blog.html", "r", encoding='utf-8') as f:
    html_string = f.read()
# data
st.markdown(''' ###### Postado em: 29/09/2024 - 12:00 ''')
#
# 
components.html(html_string, height=4000)
st.html("<a href='https://l.instagram.com/?u=https%3A%2F%2Fbit.ly%2FFalarComInacio&e=AT3IhR-X_c2-jVZnNXoFLuKpJXR91OWiLXu4aQz2_vQJedXyPzwqtyFFgZa7QYidlhGAQ0PS4u2f1QQJX-IVTF7Qyl6YeO67vpiY1w' target='_blank'>Conheça meu Github</a>")