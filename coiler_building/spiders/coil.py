import scrapy


class CoilSpider(scrapy.Spider):
    name = 'coil'
    allowed_domains = ['cbia-fl.builderfusion.com']
    start_urls = ['https://cbia-fl.builderfusion.com/bf/website/directory/index.jsp']

    def parse(self, response):
        for data in response.xpath('//a[@target="_blank"]'):
            name = data.xpath('.//text()').get()
            print(name)
        
