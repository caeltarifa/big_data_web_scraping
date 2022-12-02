import scrapy


class BigDataWebscrapingItem(scrapy.Item):
    root_url = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    file_title_web = scrapy.Field()
    file_stored_name = scrapy.Field()
    file_down_url = scrapy.Field()

    file_format = scrapy.Field()
    file_size = scrapy.Field()
    file_dimension = scrapy.Field()
    
    file_urls = scrapy.Field()
    files = scrapy.Field
    #pass
