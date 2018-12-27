import scrapy
import requests
from scrapy import Request
from urllib import parse
from ArticleSpider.items import WzvtcItem


class WzvtcSpider(scrapy.Spider):
    name = 'infoq'
    allowed_domains = ['https://www.infoq.cn/']
    start_urls = ['https://www.infoq.cn/']
    main_url = 'https://www.infoq.cn/public/v1/my/recommond'

    User_Agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"

    headers = {
        "Accept": "application/json,text/plain,*/*",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": '11',
        "Content-Type": "application/json",
        "Host": "www.infoq.cn",
        "Origin": "https://www.infoq.cn",
        "Pragma": "no-cache",
        "Referer": "https://www.infoq.cn/",
        "User-Agent": User_Agent
    }

    def parse(self, response):
        cookies = requests.utils.dict_from_cookiejar(requests.get(url=response.url).cookies)['SERVERID']
        cookies = 'SERVERID='+cookies

        self.headers.update({
            "Cookie": cookies
        })
        print(self.headers)
        yield scrapy.Request(self.main_url, headers=self.headers, callback=self.url_json)

    def url_json(self, response):
        print(response.url)
