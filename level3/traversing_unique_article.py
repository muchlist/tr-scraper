import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

pages = set()


def get_links(page_url):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(page_url))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id='mw-content-text').find_all('p')[0])
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('this page is missing something! continuing.')

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # kita memiliki page baru
                new_page = link.attrs['href']
                print('-' * 20)
                print(new_page)
                pages.add(new_page)
                get_links(new_page)


get_links('')
