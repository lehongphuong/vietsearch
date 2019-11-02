import scrapy
import json
import os

class KhoaHocSpider(scrapy.Spider):
    name = "khoahoc"

    def start_requests(self): 
        with open('list-page.html', 'r', encoding='utf8') as f:
            urls = f.readlines()
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)  

    def parse(self, response): 
        # Define variable
        filename = 'khoa-hoc1.json'  
        title = response.css('h1.title_news_detail::text').get().strip()
        content = response.css('article.content_detail').get()
        public_date = response.css('span.time::text').get()
        news = {'title':title,'content':content,'public_date':public_date} 
        list_news = []

        # Read data json and append new data to list_news
        with open(filename,'r', encoding='utf8') as f:
            list_news = f.readline()
            if list_news != '':
                list_news = json.loads(list_news)
                list_news.append(news)
            else:
                list_news = []
                list_news.append(news) 

            list_news = json.dumps(list_news)

        # Write data to json
        with open(filename,'w', encoding='utf8') as f:
            f.write(list_news)

        self.log('Saved file %s' % filename)