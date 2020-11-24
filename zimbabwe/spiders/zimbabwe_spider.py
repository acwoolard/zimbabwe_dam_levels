import scrapy
import os.path

class zimbabweSpider(scrapy.Spider):
    name = 'zimbabwe'
    start_urls = ['https://www.zinwa.co.zw/dam-levels/']

    def parse(self, response):
	
        coords_dict = {}

        current_directory = os.path.dirname(__file__)
        parent1 = os.path.split(current_directory)[0]
        parent2 = os.path.split(parent1)[0]
        dict_path = os.path.join(parent2,"dam_coords.txt")

        f = open(dict_path,mode='r')

        line = f.readline()
        while line:
            coords_dict[line.split(",")[0]]=[line.split(",")[1],line.split(",")[2]]
            line = f.readline()
    
        f.close()

        for row in response.xpath('//*[@class="jtTableContainer jtrespo-scroll  "]//tbody/tr')[1:]:
            name=row.xpath('td[1]//text()').extract_first()
            lon = 0
            lat = 0
            if name in coords_dict.keys():
                lon = coords_dict[name][0]
                lat = coords_dict[name][1][:-1]
            yield {
                'name' : name,
                'longitude' : lon,
                'latitude' : lat,
                'full': row.xpath('td[2]//text()').extract_first(),
                'current' : row.xpath('td[3]//text()').extract_first(),
	    }
