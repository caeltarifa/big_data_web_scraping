import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor 
from scrapy import Selector
import datetime

from big_data_webscraping.items import BigDataWebscrapingItem
from big_data_webscraping.spiders.class_selenium_xpath import selenium_scrapy


class IneClSpider(CrawlSpider):
    name = 'ine_cl'
    allowed_domains = ['www.ine.gob.cl']
    start_urls = ['https://www.ine.gob.cl/']

    link_extractor = LinkExtractor(allow=r'estadisticas/')

    rules = (
        Rule(link_extractor, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        
        A = "//a[contains(@href,'xls') or contains(@href,'pdf') or contains(@href, 'csv') or contains(@href, 'dta') or contains(@href, 'sav')]" 
        B = "//span[contains(@class, 'titulo')]/text() " 
        B = "//a/*[last()]/text() "
        C = '//*[@id="Content"]/div[3]/div'

        file_url = response.xpath(A)

        if file_url:
            a_nodes = file_url.xpath(A).getall()
            a_nodes = self.remove_duplicates(a_nodes)
            
            #Collecting files from the page
            #data_static = self.collect_superficial_data(a_nodes, response, B)
            names__list = []
            for a in a_nodes:
                new_node = Selector(text=a)
                childs = new_node.xpath("//a/*")
                
                if len(childs.getall())>=1:
                    name_file_childs = new_node.xpath(B).getall()[0]
                else:
                    name_file_childs = new_node.xpath("//a/text()").getall()[0]

                names__list.append(
                    ( 
                    response.urljoin(new_node.xpath('//a/@href').getall()[0]),
                    name_file_childs
                    )
                )
                
                url_file_store = response.urljoin(response.urljoin(new_node.xpath('//a/@href').getall()[0]))
                url_file_store = url_file_store if not '?' in url_file_store else url_file_store.split('?')[0]
                
                file = BigDataWebscrapingItem()
                file['date'] = str(datetime.datetime.now().date()) 
                file['time'] = str(datetime.datetime.now().time().strftime('%H:%M:%S')) 
                file['root_url'] = response.url
                file['file_title_web'] = name_file_childs
                file['file_stored_name'] = url_file_store.split('/')[-1]
                file['file_down_url'] = url_file_store
                file['file_format'] = url_file_store.split('/')[-1].split('.')[1]
                file['file_urls'] = [url_file_store]

                yield file
            
            #Collecting files from dynamic events into panels
            #data_dynamic = self.collect_dynamic_data(response, C)

            file_url = response.xpath(C)
            if file_url:
                extra_crawled_data = selenium_scrapy()
                list_response = extra_crawled_data.click_exploring_ine(response.url)

                for dict in list_response:
                    file = BigDataWebscrapingItem()
                    file['root_url'] = response.url
                    file['date'] = str(datetime.datetime.now().date()) 
                    file['time'] = str(datetime.datetime.now().time().strftime('%H:%M:%S')) 
                    file['file_title_web'] = dict['name']
                    file['file_stored_name'] = dict['file_name']
                    file['file_down_url'] = dict['link']
                    file['file_format'] = dict['file_format']
                    file['file_size'] = dict['file_size']
                    file['file_dimension'] = dict['file_dimension']
                    file['file_urls'] = [dict['link']]

                    yield file                                          

    def remove_duplicates(self, list):
        set_ = set()
        for i in list:
            if not i in set_:
                set_.add(str(i).strip())
        return sorted(set_)