import requests
from bs4 import BeautifulSoup

result = requests.get("https://pycon.jp/2016/ja/schedule/talks/list/")
soup = BeautifulSoup(result.text, "html.parser")
presentation_html_list = soup.find_all("div", class_="presentation")

for presentation_html in presentation_html_list:
    print(presentation_html.h3.get_text())
