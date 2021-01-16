from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# Mendapatkan daftar semua internal link di dalam halaman
# def get_internal_links(bs, include_url):
#     include_url = f'{urlparse(include_url).scheme}://{urlparse(include_url).netloc}'
#     internal_link = []
#     # dapatkan semua link yang dimulai dengan a
#     for link in bs.find_all('a', href= re.compile('^(/|.*'+include_url+')')):
#         if link.attrs['href']