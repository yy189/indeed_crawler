# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import json

class ScalesharkspiderPipeline(object):
    def __init__(self):
        self.file = open('startups.csv', 'w')
        fieldnames = ['organization_name', 'categories', 'headquarters_location', 'description']
        self.writer = csv.DictWriter(self.file, fieldnames=fieldnames)
        self.writer.writeheader()
        # self.csvwriter = csv.writer(self.file)
        # self.csvwriter.writerow(['organization_name', 'categories', 'headquarters_location', 'description'])

    def process_item(self, item, spider):
        self.writer.writerow({'organization_name': item['organizationName'],
                              'categories': item['categories'],
                              'headquarters_location': item['headquartersLocation'],
                              'description': item['description']})
        # print(item)
        # row = zip(item['organizationName'], item['categories'], item['headquartersLocation'], item['description'])
        
        # self.csvwriter.writerow(",".join(item))
            
        return item

    def close_spider(self, spider):
        self.file.close()
    
    # def __init__(self):
    #     self.file = open('teacher.json', 'wb')
    #
    # def process_item(self, item, spider):
    #     content = json.dumps(dict(item), ensure_ascii=False) + "\n"
    #     self.file.write(content)
    #     return item
    #
    # def close_spider(self, spider):
    #     self.file.close()
    #
