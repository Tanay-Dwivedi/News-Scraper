import streamlit as st
from bs4 import BeautifulSoup
import requests

url = "https://sarkaripariksha.com/gk-and-current-affairs/2022/january/1/1"

req = requests.get(url)

soup = BeautifulSoup(req.text, "html.parser")

news_list = soup.find_all("div", class_="examlist-details-img-box")

st.markdown(
    """
<h1 style='text-align:center'>News Scrapper</h1>
""",
    unsafe_allow_html=True,
)
st.write("##")

st.image("news_img.png", use_column_width="auto")

for news_item in news_list:
    a_tag = news_item.find("h2").find("a")

    news_title = a_tag.get_text(strip=True)
    href_link = a_tag["href"]

    st.write(f"Title: {news_title}")
    st.write(f"Link: {href_link}")
