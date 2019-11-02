import scrapy
import ast

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    def start_requests(self):
        urls = [
            'https://ketqua.net/xo-so-mien-bac',
            'https://ketqua.net/xo-so-mien-trung',
            'https://ketqua.net/xo-so-mien-nam'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1] 
        table = response.css('td::text').re('[^\n]*')  
        table1 = table
        table = filter(lambda x: x!='',table)
        print(table)
        page = page.replace('-','_')
        yield {page: '||'.join(table)}  
        yield {page+'1': '||'.join(table1)}  

    # name = "quotes" 
 
    # start_urls = [
    #     'https://ketqua.net/xo-so-mien-bac/',
    #     'https://ketqua.net/xo-so-mien-trung',
    #     'https://ketqua.net/xo-so-mien-nam'
    # ] 

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     table = response.css('td::text').re('[^\n]*')
    #     table = filter(lambda x: x!='',table)
    #     print(table)
    #     yield {page: '||'.join(table)} 