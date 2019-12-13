import requests

result = requests.get("https://www.yokohama-stadium.co.jp/")
print(result.text)

