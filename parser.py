import requests, lxml
from bs4 import BeautifulSoup as bs

url="https://coinmarketcap.com"

headers= {
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
    "X-Requested-Width":"XMLHttpRequest"
}

resp = requests.get(url,headers=headers)

soup = bs(resp.text, "lxml")

tbody = soup.find("tbody")
coins = tbody.find_all("tr")

for coin in coins:
    name = coin.find(class_="coin-item-symbol")
    price = coin.find(class_="sc-8bda0120-0 dskdZn")

    if name:
        print(f"{name.text}: {price.text}")