import streamlit as st
from bs4 import BeautifulSoup
import requests
from streamlit_card import card

st.markdown(
    """
<h1 style='text-align:center'>News Scrapper</h1>
""",
    unsafe_allow_html=True,
)
st.write("##")

st.image("news_img.png", use_column_width="auto")
st.write("##")

st.write("## Select the Date: ")
st.write("##")

year, month, day = st.columns(3)
year_select = year.selectbox("Select year:", options=["2024", "2023", "2022"])
month_select = month.selectbox(
    "Select month:",
    options=[
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    ],
)
day_select = day.selectbox("Select day: ", options=[str(i) for i in range(1, 32)])
st.write("##")
toggle_btn = st.toggle("Hindi")
st.write("##")

Scrap_btn = st.button("Scrap")


st.write("##")
str_date = str(day_select)
if str_date[-1] == "1" and str_date != "11":
    st.write(f"### News for the date {day_select}st  {month_select}, {year_select}")
elif str_date[-1] == "2" and str_date != "12":
    st.write(f"### News for the date {day_select}nd {month_select}, {year_select}")
elif str_date[-1] == "3" and str_date != "13":
    st.write(f"### News for the date {day_select}rd {month_select}, {year_select}")
else:
    st.write(f"### News for the date {day_select}th {month_select}, {year_select}")

box_style = """
    <style>
        .custom-box {
            padding: 10px;
            border: 2px solid white;
            border-radius: 10px;
            background-color: black;
            color: white;
            margin-bottom: 10px;
        }
        .custom-box a {
            color: #00FFFF !important;
            text-decoration: none !important;
            font-weight: bold !important;
        }
    </style>
"""

count = 1
if Scrap_btn:
    text_language = "1"
    if toggle_btn:
        text_language = "2"
    url = (
        "https://sarkaripariksha.com/gk-and-current-affairs/"
        + year_select
        + "/"
        + month_select
        + "/"
        + str(day_select)
        + "/"
        + text_language
        + "/"
    )
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    news_list = soup.find_all("div", class_="examlist-details-img-box")
    for news_item in news_list:
        a_tag = news_item.find("h2").find("a")
        p_tag = news_item.find("p")

        news_title = a_tag.get_text(strip=True)
        href_link = a_tag["href"]
        st.markdown(box_style, unsafe_allow_html=True)
        st.markdown(
            f"""<div class="custom-box">{count}- <a href="{href_link}">{news_title}</a></div>""",
            unsafe_allow_html=True,
        )
        count = count + 1
