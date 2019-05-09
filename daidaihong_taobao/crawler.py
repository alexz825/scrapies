"""
爬虫
"""
import urllib
import urllib.request
import re
import js2xml
from js2xml.utils.vars import get_vars
from bs4 import BeautifulSoup

# """
def requestTaoBao(url):
    user_agent = "Mozilla / 5（X11；U；Linux i686）Gecko/2008070208火狐20071127 / 2.0.0.11"
    req = urllib.request.Request(
        url, data=None, headers={"user-agent": user_agent.encode("utf8")}
    )
    response = urllib.request.urlopen(req)
    return response.read()


def getShopAllGoods(content):
    # 解析
    soup = BeautifulSoup(content, "lxml", from_encoding="gbk")
    more_btn_url = soup.find(name="a", class_="show-more border-radius hotsell_desc")[
        "href"
    ]
    soup2 = BeautifulSoup(
        requestTaoBao("http:" + more_btn_url), "lxml", from_encoding="gbk"
    )
    print(soup2.prettify)


def spider_taobao(url):

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.3",
        "Referer": "https://item.taobao.com/item.htm",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Connection": "keep-alive",
    }

    goods_id = re.findall("id=(\d+)", url)[0]
    req = urllib.request.Request(url, data=None, headers=headers)
    res = urllib.request.urlopen(req).read().decode("gbk", "ignore")

    # soup = BeautifulSoup(res, "lxml", from_encoding="gbk")
    # script = soup.select("head script")[0].string
    # script_text = js2xml.parse(script)
    # script_tree = js2xml.pretty_print(script_text)

    # print(script_tree)
    # print(get_vars(script_text))

    # 请求下来的网页里面有个script，script里面包含了g_config变量，里面有详情描述的url，请求即可以得到desc的内容
    try:
        title = re.findall('<h3 class="tb-main-title" data-title="(.*?)"', res)
        title = title[0] if title else None
        line_price = re.findall('<em class="tb-rmb-num">(.*?)</em>', res)[0]

        # 抓取淘宝商品真实价格，该数据是动态加载的
        purl = "https://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId={}&modules=price,xmpPromotion".format(
            goods_id
        )
        price_req = urllib.request.Request(purl, data=None, headers=headers)
        price_res = urllib.request.urlopen(price_req).read().decode("gbk", "ignore")
        data = list(set(re.findall('"price":"(.*?)"', price_res)))
        # data列表中的价格可能是定值与区间的组合，也可能只是定值，而且不一定有序
        real_price = ""
        for t in data:
            if "-" in t:
                real_price = t
                break
        if not real_price:
            real_price = sorted(map(float, data))[0]

        # 获取描述
        descUrl = re.findall(
            "descUrl          : location.protocol==='http:' \? '(.*?)' : ", res
        )[0]
        descUrl = "http:" + descUrl
        desc_req = urllib.request.Request(descUrl, data=None, headers=headers)
        desc_res = urllib.request.urlopen(desc_req).read().decode("gbk", "ignore")
        desc_text = re.findall("var desc='(.*?)';", desc_res)[0]

        # 抓取评论数据，该数据也是动态加载的
        # comment_url = "https://rate.tmall.com/list_detail_rate.htm?itemId={}&sellerId=880734502&currentPage=1".format(
        #     goods_id
        # )
        # comment_data = urllib2.urlopen(comment_url).read().decode("GBK", "ignore")
        # temp_data = re.findall('("commentTime":.*?),"days"', comment_data)
        # temp_data = (
        #     temp_data
        #     if temp_data
        #     else re.findall('("rateContent":.*?),"reply"', comment_data)
        # )
        # comment = ""
        # for data in temp_data:
        #     comment += data.encode("utf-8")
        # comment = comment if comment else "暂无评论"

        print("商品名:", title)
        print("划线价格:", line_price)
        print("真实价格:", real_price)
        print("商品链接:", url)
        print("描述", desc_text)
        # print("部分评论内容:", comment)
    except Exception as e:
        print("数据抽取失败!!!", e)


# """

# def seleniumRequest(url):
#     driver = webdriver.Chrome()
#     wait = WebDriverWait(driver, 10)
#     item = driver.find_elements_by_css_selector('dl.item')
#     try:
#         driver.get(url)
#         wait.until(EC.presence_of_element_located(By.CSS_SELECTOR, ''))
#     except TimeoutException:
#         return ""
#     print(len(item))

shop_url = "https://shop458578821.taobao.com/search.htm?spm=a1z10.1-c-s.0.0.302bce58yHcYMS&search=y&orderType=hotsell_desc"

if __name__ == "__main__":
    # first_request_data = requestTaoBao(shop_url)
    # getShopAllGoods(first_request_data)
    spider_taobao(
        "https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4023-17342846451.4.3669531aLI2TlG&id=580724871322"
    )
