"""
爬取店铺所有商品页面
"""
import scrapy

class TaobaoShopSpider(scrapy.Spider):
    """
    根据店铺页面里面的所有商品，获取所有的商品列表
    """
    name = "taobao_shop"
    def start_requests(self):
        """
        开始请求
        """
        urls = ['https://shop458578821.taobao.com/search.htm?spm=a1z10.1-c-s.0.0.4e6c0d1BNXfKp&search=y']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        解析请求回来的
        """
        print(response.css('#J_ShopSearchResult > div > div.shop-hesper-bd.grid'))

        
