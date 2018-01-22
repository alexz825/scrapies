"""
爬虫
"""
import urllib
import urllib.request
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# 分析得到，不能直接爬虫店铺全部商品页面，因为全部商品是通过
# https://shop458578821.taobao.com/i/asynSearch.htm得到的
# 可是其中有cookie，和第一次请求返回的cookie并不同，不知道如果去得到新cookie，只能放弃然后使用模拟浏览器方法去爬虫了
"""
def requestTaoBao(url):
    user_agent = 'Mozilla / 5（X11；U；Linux i686）Gecko/2008070208火狐20071127 / 2.0.0.11'
    req = urllib.request.Request(url, data=None, headers={
        'user-agent': user_agent
    })
    response = urllib.request.urlopen(req)
    return response.read()
    
def getShopAllGoods(content):
    #解析
    soup = BeautifulSoup(content, "lxml", from_encoding='gbk')
    more_btn_url = soup.find(name='a', class_='show-more border-radius hotsell_desc')['href']
    soup2 = BeautifulSoup(requestTaoBao('http:' + more_btn_url), 'lxml', from_encoding='gbk')
    print(soup2.prettify)
"""

def seleniumRequest(url):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    item = driver.find_elements_by_css_selector('dl.item')
    try:
        driver.get(url)
        wait.until(EC.presence_of_element_located(By.CSS_SELECTOR, ''))
    except TimeoutException:
        return ""
    print(len(item))

shop_url = 'https://shop458578821.taobao.com/search.htm?spm=a1z10.1-c-s.0.0.302bce58yHcYMS&search=y&orderType=hotsell_desc'
seleniumRequest(shop_url)