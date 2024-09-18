import streamlit as st
from scrape import scrape_website,split_dom_content,clean_body_content,extract_body_content

st.title("ScrapeAI")
url = st.text_input("Enter a Website URL: ")

if st.button("Scrape Site"):
    st.write("scraping the Websit