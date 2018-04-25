import urllib
import urllib.request
from bs4 import BeautifulSoup
import socket
import sqlite3

def testIsValid(ip, port):
    socket.setdefaulttimeout(2)
    proxy = ip + ':' + port
    proxy_handler = urllib.request.ProxyHandler({'http': proxy})
    opener = urllib.request.build_opener(proxy_handler)
    urllib.request.install_opener(opener)
    try:
        html = urllib.request.urlopen('http://www.baidu.com')
        # 存入数据库
        return True
    except Exception:
        return False

def IPspider(numpage):  
    url='http://www.xicidaili.com/nn/'  
    user_agent = 'IP'  
    headers = {'User-agent': user_agent}  
    for num in range(1, numpage+1):  
        ipurl = url + str(num)  
        print('Now downloading the '+ str(num*100)+' ips')
        request = urllib.request.Request(ipurl, headers=headers)  
        content = urllib.request.urlopen(request).read()
        bs = BeautifulSoup(content,'html.parser')  
        res = bs.find_all('tr')  
        for item in res:  
            try:  
                temp = []
                tds = item.find_all('td')
                temp.append(tds[1].text)
                temp.append(tds[2].text)
                print(temp, testIsValid(temp[0], temp[1]))
            except IndexError:  
                    pass
#假设爬取前十页所有的IP和端口  
IPspider(10)