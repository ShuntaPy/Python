import requests
from bs4 import BeautifulSoup

result = requests.get("https://bang-dream.com/")
soup = BeautifulSoup(result.text, "html.parser")
img = soup.find_all('img')
print(img)
