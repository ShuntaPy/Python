import requests
from bs4 import BeautifulSoup

result = requests.get("http://bang-dream-news.com/")
soup = BeautifulSoup(result.text, "html.parser")
title = soup.title.string
print(title)
