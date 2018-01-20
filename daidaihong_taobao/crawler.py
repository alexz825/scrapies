"""
爬虫
"""
import urllib
import urllib.request
import asyncio
import re
import requests
from bs4 import BeautifulSoup

def requestTaoBao(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    req = urllib.request.Request(url, data=None, headers={
        'user-agent': user_agent
    })
    response = urllib.request.urlopen(req)
    return response.read()
    
def getShopAllGoods(content):
    #解析
    soup = BeautifulSoup(content, "lxml", from_encoding='utf-8')
    more_btn_url = soup.find(name='a', class_='show-more border-radius hotsell_desc')['href']
    soup2 = BeautifulSoup(requestTaoBao('http:' + more_btn_url), 'lxml', from_encoding=None)
    print(soup2.prettify)

shop_url = 'https://shop458578821.taobao.com/search.htm'
getShopAllGoods(requestTaoBao(shop_url))
# print(requests.get(shop_url).text)
