import re
from urllib.request import urlopen

from bs4 import BeautifulSoup


def url_crawler(bs):
    for link in bs.find_all('a'):
        if 'href' in link.attrs:
            print(link.attrs['href'])


def url_crawler_with_filter(bs):
    for link in bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs:
            print(link.attrs['href'])


if __name__ == '__main__':
    html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
    b_soup = BeautifulSoup(html, 'html.parser')
    url_crawler_with_filter(b_soup)
