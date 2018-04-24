import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.dcard.tw/f'
resp = requests.get(url) #回傳為一個request.Response的物件
print(resp.status_code)
soup = BeautifulSoup(resp.text, 'html.parser')
dcard_title = soup.find_all('h3', re.compile('PostEntry_title_'))
print('Dcard 熱門前十文章標題：')
for index, item in enumerate(dcard_title[:100]):
    print("{0:2d}. {1}".format(index + 1, item.text.strip()))