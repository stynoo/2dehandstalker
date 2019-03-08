import requests
from bs4 import BeautifulSoup

#page = requests.get("https://www.2dehands.be/markt/2/gravis%20ultrasound/")
page = requests.get("https://www.2dehands.be/markt/2/my%20little%20pony/")

soup = BeautifulSoup(page.text, "html.parser")

if soup.find(class_="panel has-icon no-results"):
    print("no results found")
elif soup.find(class_="search-result"):
    print("results found")
    items = soup.find_all("article")
    for item in items:
        # print(item.prettify())
        item_name = item.find(class_="listed-adv-item-link").contents[0].strip()
        item_date = item.find(class_="listed-item-date").contents[0].strip()
        item_price = item.find(class_="listed-item-price").contents[0].strip()
        item_url = item.find(class_="listed-adv-item-link").get("href").strip()
        print(item_date + "||" + item_price + "||" + item_name + "||" + item_url)
