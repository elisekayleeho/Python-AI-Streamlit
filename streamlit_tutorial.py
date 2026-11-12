import streamlit as st

st.set_page_config(page_title="Tab Title")

st.title("Streamlit Tutorial")

st.text("Created by Elise")

st.info("This is an info box")

st.success("Success!")

st.error("Error:(")

st.markdown("<h1> style='color: Hello, World!</h1>", unsafe_allow_html = True)

st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
