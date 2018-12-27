import scrapy
from scrapy import Request
from urllib import parse
from ArticleSpider.items import WzvtcItem

class WzvtcSpider(scrapy.Spider):
    name = 'wzvtc'
    allowed_domains = ['www.wzvtc.com']
    start_urls = ['http://cs.wzvtc.cn/xwzx/jstzgg/index.html']

    def parse(self, response):

        post_url_list = response.css('.page_list .page_list_title a::attr(href)').extract()
        post_title = response.css('.page_list .page_list_title a::text').extract()
        post_date = response.css('.page_list .page_list_date').extract()


        for post_url in post_url_list:

            post_url = 'http://cs.wzvtc.cn'+post_url

            yield Request(url=post_url, callback=self.parse_detail,dont_filter=True)

        try:

            next_url = response.css('.paging .pg_next a::attr(href)').extract()[0]

        except Exception as e:

            print(e)

        if next_url:

            yield Request(url=parse.urljoin('http://cs.wzvtc.cn/xwzx/jstzgg/',next_url),callback=self.parse,dont_filter=True)




    def parse_detail(self,response):

        url = response.url
        title = response.css('#ShowArticle #ShowArticle_title::text').extract()[0]
        auth = response.css('#ShowArticle ul #ShowArticle_type::text').extract()[0].split()
        create_date = (response.css('#ShowArticle ul #ShowArticle_type::text').extract()[1].split('：'))[1]
        content_url = response.css('#ShowArticle ul #ShowArticle_Content p a::attr(href)').extract()[0]


        if not content_url:

            content_url = response.css('#ShowArticle #ShowArticle_Content p::text').extract()

        # print(content_url)

        auth = ''.join(auth)

        wzvtc_item = WzvtcItem()

        wzvtc_item['url'] = url
        wzvtc_item['title'] = title
        wzvtc_item['auth'] = auth
        wzvtc_item['create_date'] = create_date
        wzvtc_item['content_url'] = content_url

        return wzvtc_item