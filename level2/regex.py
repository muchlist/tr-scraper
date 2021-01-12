"""

1. a setidaknya 1 kali
2. b persis 5 kali
3. c beberapa kali pasang
4. d atau e pada akhir kata

ex : aaaabbbbbccccd, aabbbbbcce

rgex = aa*bbbbb(cc)*(d|e)

aa*  :
    a setidaknya 1 kali dilanjut dengan a* yang artinya beberapa huruf a termasuk 0 a . dengan begitu
    digaransi bahwa setidaknya ada a 1 kali
bbbbb :
    5 b persis
(cc)* :
    dapat mempunyai sejumlah pasangan c atau 0 c
(d|e) :
    d atau e
"""

import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src': re.compile('\.\./img/gifts/img.*\.jpg')})
# images = bs.find_all('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])

"""
../img/gifts/img1.jpg
../img/gifts/img2.jpg
../img/gifts/img3.jpg
../img/gifts/img4.jpg
../img/gifts/img6.jpg
"""