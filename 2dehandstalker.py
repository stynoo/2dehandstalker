#!/bin/env python
import argparse
import json
import requests
from bs4 import BeautifulSoup


def get_parsed_arguments():
  parser = argparse.ArgumentParser(description='Get 2dehands items')
  parser.add_argument('--filter', help='optional search filter')
  parser.add_argument('--pages', help='optional amount of pages')
  return parser.parse_args()


def get_2dehands_items(query = None, pages = 1):
    results = []

    for page in range(0, int(pages)):
        offset = (38 * page)
        page = requests.get(f'https://www.2dehands.be/markt/2/${query}/?offset=${offset}')
        soup = BeautifulSoup(page.text, "html.parser")
        
        if soup.find(class_="panel has-icon no-results"):
            return None
        elif soup.find(class_="search-result"):
            items = soup.find_all("article")
            for item in items:
                item_json = {
                    'name':     item.find(class_="listed-adv-item-link").contents[0].strip(),
                    'date':     item.find(class_="listed-item-date").contents[0].strip(),
                    'price':    item.find(class_="listed-item-price").contents[0].strip(),
                    'url':      item.find(class_="listed-adv-item-link").get("href").strip(),
                    'image':    item.find(class_="item-center-image").get("src").strip()
                }
                if item_json:
                    results.append(item_json)
        offset+=38
    return results


if  __name__ == "__main__":
   args = get_parsed_arguments()
   print(json.dumps(get_2dehands_items(args.filter, args.pages), 
                    sort_keys=True, indent=4, ensure_ascii=False))
