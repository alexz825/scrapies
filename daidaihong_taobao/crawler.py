"""
爬虫
"""
import urllib
import urllib.request
import asyncio
import re
from bs4 import BeautifulSoup

def requestTaoBao(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    req = urllib.request.Request(url, data=None, headers={
        'User-Agent': user_agent
    })
    response = urllib.request.urlopen(req)
    return response.read()
    
def getShopAllGoods(content):
    #解析
    soup = BeautifulSoup(content, "lxml")
    # print(soup.prettify())
    reg = re.compile('class="item')
    print(reg)
    item = soup.find_all(reg)
    print(item)

shop_url = 'https://shop458578821.taobao.com/search.htm?spm=a1z10.1-c-s.0.0.361cee58SIdQEK&search=y&orderType=hotsell_desc'
getShopAllGoods(requestTaoBao(shop_url))



