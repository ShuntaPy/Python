import requests
from bs4 import BeautifulSoup

result = requests.get("http://bang-dream-news.com/")
soup = BeautifulSoup(result.text, "html.parser")
container = soup.find("div", class_=("container"))
print(container)
