import requests

from bs4 import BeautifulSoup

num = input()
url = input()
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
paragraphs = soup.find_all('h2')

print(paragraphs[int(num)].text)
