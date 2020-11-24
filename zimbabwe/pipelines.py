# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os.path


class ZimbabwePipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        coords_dict = {}

        current_directory = os.path.dirname(__file__)
        parent = os.path.split(current_directory)[0]
        dict_path = os.path.join(parent,"dam_coords.txt")

        f = open(dict_path,mode='r')

        line = f.readline()
        while line:
            coords_dict[line.split(",")[0]]=[line.split(",")[1],line.split(",")[2]]
            line = f.readline()
    
        f.close()

        lon = 0
        lat = 0
        if adapter['name'] in coords_dict.keys():
            lon = coords_dict[adapter['name']][0]
            lat = coords_dict[adapter['name']][1][:-1]

        adapter["longitude"]=lon
        adapter["latitude"]=lat

        return item
