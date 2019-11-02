import scrapy


class KhoaHocSpider(scrapy.Spider):
    name = "khoahocpage"

    def start_requests(self): 
        url = 'https://vnexpress.net/khoa-hoc'  
        # yield scrapy.Request(url=url, callback=self.parse) 

        for i in range(1,1548):
            url_next = url + '-p' + str(i)
            yield scrapy.Request(url=url_next, callback=self.parse) 

    def parse(self, response): 
        filename = 'khoa-hoc-page.html'
        with open(filename, 'a') as f:
            for page in response.css('h4.title_news a::attr(href)'):
                next_page = page.get() + '\n'

                # Check duplicate url
                if(('#box_comment' in next_page)==False):
                    f.write(next_page)
        
        self.log('Saved file %s' % filename)