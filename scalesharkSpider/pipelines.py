# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import json

class ScalesharkspiderPipeline(object):
    def __init__(self):
        self.f = open('startups.csv', 'wb')
        self.csvwriter = csv.writer(self.f, delimiter=',')
        self.csvwriter.writerow(['organization_name', 'categories', 'headquarters_location', 'description'])

    def process_item(self, item, spider):
        rows = zip(item['organizationName'], item['categories'], item['headquartersLocation'], item['description'])
        print(rows[0])
        
        for row in rows:
            self.csvwriter.writerow(row)
            
        return item

    def close_spider(self, spider):
        self.f.close()
    
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
