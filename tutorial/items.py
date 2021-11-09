import scrapy


class NewsItem(scrapy.Item):
    title = scrapy.Field()
    imgUrl = scrapy.Field()
    newTime = scrapy.Field()
