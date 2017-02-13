import urllib.request as request
import re
from bs4 import BeautifulSoup as bs

"""查询wiki中所有的词条"""
# https://en.wikipedia.org/wiki/Main_Page
file = open('E:\\url.txt', 'a', encoding='utf-8')

def putUrl(u):
    urlList = []
    page = request.urlopen(u).read().decode('utf-8')
    # print(page)
    soup = bs(page, 'html.parser')
    urls = soup.findAll('a', href=re.compile(r'^/wiki/'))
    for url in urls:
        if not re.search(r'\.(jpg|JPG)$', url['href']):
            str = url.get_text() + '---->' + 'https://en.wikipedia.org' + url['href'] + '\n'
            file.write(str)
            print(str)
            urlList.append('https://en.wikipedia.org' + url['href'])
    return urlList
for url in putUrl('https://en.wikipedia.org/wiki/Main_Page'):
    putUrl(url)