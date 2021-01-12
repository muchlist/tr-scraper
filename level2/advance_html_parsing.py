from urllib.error import HTTPError
from urllib.request import urlopen

from bs4 import BeautifulSoup

html = None
try:
    html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
except HTTPError as e:
    print(e)

name_list = []
try:
    bs = BeautifulSoup(html.read(), 'html.parser')
    name_list = bs.find_all('span', {'class': 'green'})
    # name_list = bs.find_all('span', {'class': {'green', 'red'}})
except AttributeError as e:
    print(e)
for name in name_list:
    print(name.get_text())
