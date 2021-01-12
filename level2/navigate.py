from urllib.request import urlopen

from bs4 import BeautifulSoup


def find_children(bs):
    for child in bs.find('table', {'id': 'giftList'}).children:
        print(child)


def find_next_sibling(bs):
    for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:  # will skip the title
        print(sibling)


def find_parent(bs):
    print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

    """
    
    result $15.00
    
    <td> 3. ke sibling sebelumnya
        $15.00 4. get.text()
    </td>
    <td> 2. ke parent
        <img src="../img/gifts/img1.jpg">  1. memilih tag image
    </td>
    """


if __name__ == '__main__':
    html = urlopen('http://www.pythonscraping.com/pages/page3.html')
    b_soup = BeautifulSoup(html, 'html.parser')
    find_parent(b_soup)
