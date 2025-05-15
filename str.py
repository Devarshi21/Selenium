import streamlit as st
from bse_ann import scrapper, company

#scrapper()
st.write("## List of Companies")


st.button("Scrap BSE Announcements", on_click=scrapper)
st.write("### Companies")
for i in company:
    st.write(i)