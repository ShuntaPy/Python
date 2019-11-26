import requests
from bs4 import BeautifulSoup

result = requests.get("https://pycon.jp/2016/ja/schedule/talks/list/")
soup = BeautifulSoup(result.text, "html.parser")
presentation_html_list = soup.find_all("div", class_="presentation")

print("language | title")
print("--------- | ---------")
for presentation_html in presentation_html_list:
    presentation_title = presentation_html.h3.get_text()

    if"(en)"in presentation_title:
        language = "English"
        title = presentation_title.replace("\xa0(en)", "")
    elif"(ja)"in presentation_title:
        language = "Japanese"
        title = presentation_title.replace("\xa0(ja)", "")
    print("{0}|{1}".format(language,title))
