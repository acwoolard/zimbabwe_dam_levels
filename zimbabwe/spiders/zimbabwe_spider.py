import scrapy

class zimbabweSpider(scrapy.Spider):
    name = 'zimbabwe'
    start_urls = ['https://www.zinwa.co.zw/dam-levels/']

    def parse(self, response):
	
        date = response.xpath("//*[@class='jtrt_table_MotherShipContainer']//text()").get()

        for row in response.xpath('//*[@class="jtTableContainer jtrespo-scroll  "]//tbody/tr')[1:]:
            
            yield {
                'date' : date,
                'name' : row.xpath('td[1]//text()').extract_first(),
                'full': row.xpath('td[2]//text()').extract_first(),
                'current' : row.xpath('td[3]//text()').extract_first(),
	    }
