import requests

from bs4 import BeautifulSoup

letter = 'S'
url = input()
li = BeautifulSoup(requests.get(url).content, 'html.parser').find_all('a')
blank_list = []
for list_element in li:
    if (list_element.text.startswith('S') and len(list_element.text) > 1) \
            and ('topics' in list_element.get('href') or 'entity' in list_element.get('href')):
        blank_list.append(list_element.text)

print(blank_list)
