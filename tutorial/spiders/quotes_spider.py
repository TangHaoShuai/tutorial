from tutorial.items import NewsItem
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = []

    def start_requests(self):
        urls = [
            'https://news.163.com/',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
                筛选信息的函数：
                title = 新闻标题
                imgUrl = 图片地址
                newTime = 这个新闻的时间
        """

        html_data = response.xpath('//div[@class="data_row news_article clearfix "]').getall()
        for sel in html_data:
            item = NewsItem()
            item['title'] = Selector(text=sel).xpath('//div[@class="news_title"]/h3/a/text()').get()
            item['url'] = Selector(text=sel).xpath('//div[@class="news_title"]/h3/a/@href').get()
            # url = item['url']
            # yield scrapy.Request(url=url, callback=self.parse_to)
            item['imgUrl'] = Selector(text=sel).xpath('//a[@class="na_pic"]/img/@src').get()
            item['newTime'] = Selector(text=sel).xpath('//div[@class="news_tag"]/span/text()').get()
            print("新闻标题", item['title'], "新闻地址", item['url'], "新闻图片地址", item['imgUrl'], "新闻发布时间", item['newTime'])
            yield item

    #     for i in range(10):
    #         yield scrapy.Request(url='https://www.163.com/dy/article/H1S0QHSV053469LG.html', callback=self.parse_to)
    #
    # def parse_to(self, response):
    #     html_data = response.xpath('//div[@class="post_body"]').getall()
    #     for sel in html_data:
    #         title = Selector(text=sel).xpath('//p[@id="0MR9B20I"]/text()').get()
    #         yield title
