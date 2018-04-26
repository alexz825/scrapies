import urllib
import urllib.request
from bs4 import BeautifulSoup
import socket
import csv
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
    csvfile = open('ip_pool.csv', 'w')
    writer = csv.writer(csvfile)
    
    url='http://www.xicidaili.com/nn/'  
    user_agent = 'IP'  
    headers = {'User-agent': user_agent}  
    for num in range(1, numpage+1):  
        ipurl = url + str(num)  
        print('Now downloading the '+ str(num*100)+' ips')
        request = urllib.request.Request(ipurl, headers=headers)
        try:
            content = urllib.request.urlopen(request).read()
        except Exception as ex:
            print('请求失败---', ex)
        bs = BeautifulSoup(content,'html.parser')  
        res = bs.find_all('tr')  
        for item in res:  
            try:
                temp = []
                tds = item.find_all('td')
                temp.append(tds[1].text)
                temp.append(tds[2].text)
                print(temp, testIsValid(temp[0], temp[1]))
                if testIsValid(temp[0], temp[1]):
                    writer.writerow([temp[0], temp[1]])
            except IndexError:  
                pass
        csvfile.close()
# #假设爬取前十页所有的IP和端口
IPspider(10)