import scrapy
import ast

class CompanySpider(scrapy.Spider):
    name = "company"
    
    def start_requests(self):
        # urls = [
        #     'http://danangcity.com.vn/doanh-nghiep/0.html',  
        # ]
        url = 'http://danangcity.com.vn/doanh-nghiep/' 
        for i in range(120):
            temp = url + str(i) +'.html'  
            yield scrapy.Request(url=temp, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-1]
        filename = 'doanh-nghiep-chua-co-web.txt' 
        # chưa có web
        with open(filename, 'a', encoding='utf8') as f:
            for item in response.css('div.info'): 
                temp = item.css('div.item-rows::text').getall()
                if temp[9].strip()=='':
                    if item.css('div.name-en::text').get() != None: 
                        f.write(item.css('div.name-en::text').get().strip()) 
                        f.write(temp[1].strip()+'\n')
                        f.write(temp[3].strip()+'\n')
                        f.write(temp[5].strip()+'\n')
                        f.write(temp[7].strip()+'\n')
                        f.write(temp[9].strip()+'\n')
                        f.write('Kết thúc'+'\n'+'\n')

        filename = 'doanh-nghiep-da-co-web.txt' 
        # đã có web
        with open(filename, 'a', encoding='utf8') as f:
            for item in response.css('div.info'): 
                temp = item.css('div.item-rows::text').getall()
                if temp[9].strip()!='':
                    if item.css('div.name-en::text').get() != None: 
                        f.write(item.css('div.name-en::text').get().strip()) 
                        f.write(temp[1].strip()+'\n')
                        f.write(temp[3].strip()+'\n')
                        f.write(temp[5].strip()+'\n')
                        f.write(temp[7].strip()+'\n')
                        f.write(temp[9].strip()+'\n')
                        f.write('Kết thúc'+'\n'+'\n')  

        filename = 'email-doanh-nghiep-chưa-co-web.txt'  
        # chưa có web
        with open(filename, 'a', encoding='utf8') as f:
            for item in response.css('div.info'): 
                temp = item.css('div.item-rows::text').getall()
                if temp[9].strip()=='':
                    if item.css('div.name-en::text').get() != None:  
                        f.write(temp[7].strip()+'\n')  

        filename = 'email-doanh-nghiep-da-co-web.txt' 
        # đã có web
        with open(filename, 'a', encoding='utf8') as f:
            for item in response.css('div.info'): 
                temp = item.css('div.item-rows::text').getall()
                if temp[9].strip()!='':
                    if item.css('div.name-en::text').get() != None:  
                        f.write(temp[7].strip()+'\n')  

    # def parse(self, response):
    #     page = response.url.split("/")[-1] 
    #     table = response.css('td::text').re('[^\n]*')  
    #     table1 = table
    #     table = filter(lambda x: x!='',table)
    #     print(table)
    #     page = page.replace('-','_')
    #     yield {page: '||'.join(table)}  
    #     yield {page+'1': '||'.join(table1)}  

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