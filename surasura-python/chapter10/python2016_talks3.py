

import requests
from bs4 import BeautifulSoup

result = requests.get("https://pycon.jp/2016/ja/schedule/talks/list/")
soup = BeautifulSoup(result.text, "html.parser")
presentation_html_list = soup.find_all("div", class_="presentation")

with open("pyconjp-2016-talks.txt","w",encoding="utf-8")as f:
    f.write("{0:<10}|{1}\n".format("language", "title",))
    f.write("{0:<10}|{0}\n".format("---------"))
    for presentation_html in presentation_html_list:
        presentation_title = presentation_html.h3.get_text()

        if"(en)"in presentation_title:
            language = "English"
            title = presentation_title.replace("\xa0(en)", "")
        elif"(ja)"in presentation_title:
            language = "Japanese"
            title = presentation_title.replace("\xa0(ja)", "")
    
        f.write("{0:<10}|{1}\n".format(language, title))
