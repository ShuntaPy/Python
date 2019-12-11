import requests
from bs4 import BeautifulSoup

result = requests.get("http://bang-dream-news.com/")
soup = BeautifulSoup(result.text, "html.parser")
link = soup.a.get('href')
print(link)
