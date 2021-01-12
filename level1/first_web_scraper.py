from urllib.error import HTTPError
from urllib.request import urlopen

from bs4 import BeautifulSoup


def get_title(url: str):
    try:
        html = urlopen(url)
    except HTTPError:
        return None

    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError:
        return None
    return title


title = get_title('https://meretas.com')
# title = get_title('http://www.pythonscraping.com/pages/page1.html')
if title is None:
    print('title could not be found')
else:
    print(title)
