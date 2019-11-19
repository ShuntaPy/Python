import requests

result = requests.get("https://pycon.jp/2016/ja/schedule/talks/list/")
print(result.text)
