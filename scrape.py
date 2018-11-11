# %%
from bs4 import BeautifulSoup
import requests
card_pages = 2
for card_page in range(1, card_pages+1):
    url = "http://www.roguard.net/db/cards/?page={}".format(card_page)
    response = requests.get(url)
    content = BeautifulSoup(response.content, "html.parser")

    paragraphs = content.find_all("tr")
    # print(paragraphs)
    for i in range(0, len(paragraphs)):
        item = {}
        item['name'] = paragraphs[i].find_all(
            "td")[1].find_all("div")[0].get_text()
        item['effect'] = paragraphs[i].find_all(
            "td")[2].find_all("div")[1].get_text().split('\n')
        item['loot_effect'] = paragraphs[i].find_all(
            "td")[2].find_all("div")[3].get_text().split('\n')
        print(item)

# %%
