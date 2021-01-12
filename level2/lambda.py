from urllib.request import urlopen

from bs4 import BeautifulSoup


def find_with_2_attribute(bs):
    res = bs.find_all(lambda tag: len(tag.attrs) == 2)  # return tag with 2 attribute
    for el in res:
        print(el)


def find_with_tag_text(bs):
    res = bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?')
    # res = bs.find_all('', text='Or maybe he\'s only resting?')  # persamaannya dengan lambda
    for el in res:
        print(el)

    """
    <span class="excitingNote">Or maybe he's only resting?</span>
    """


if __name__ == '__main__':
    html = urlopen('http://www.pythonscraping.com/pages/page3.html')
    b_soup = BeautifulSoup(html, 'html.parser')
    find_with_tag_text(b_soup)
