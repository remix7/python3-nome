import urllib.request as request

url = 'http://www.echoes.cn'

page = request.urlopen(url).read().decode('utf-8')

print(page)