from tutorial.items import NewsItem
import scrapy
from scrapy.selector import Selector


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["news.163.com"]

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

        # for sel in response.xpath('//div[@class="ndi_main"]/div[@class="data_row news_article clearfix "]').extract():
        #     item = NewsItem()
        #     item['title'] = sel.xpath('//div[@class="news_title"]/h3/a/text()').extract()
        #     item['imgUrl'] = sel.xpath('//a[@class="na_pic"]/img/@src').extract()
        #     item['newTime'] = sel.xpath('//div[@class="news_tag"]/span/text()').extract()
        #     print(item['title'], item['imgUrl'], item['newTime'])

        html_data = response.xpath('//div[@class="data_row news_article clearfix "]').getall()
        for sel in html_data:
            item = NewsItem()
            item['title'] = Selector(text=sel).xpath('//div[@class="news_title"]/h3/a/text()').get()
            item['url'] = Selector(text=sel).xpath('//div[@class="news_title"]/h3/a/@href').get()
            item['imgUrl'] = Selector(text=sel).xpath('//a[@class="na_pic"]/img/@src').get()
            item['newTime'] = Selector(text=sel).xpath('//div[@class="news_tag"]/span/text()').get()
            print("新闻标题", item['title'], "新闻地址", item['url'], "新闻图片地址", item['imgUrl'], "新闻发布时间", item['newTime'])
            yield item

        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')
