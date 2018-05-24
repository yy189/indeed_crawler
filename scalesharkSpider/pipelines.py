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

    def process_item(self, item, spider):
        D = {'organization_name': item['organizationName'],
             'categories': item['categories'],
             'headquarters_location': item['headquartersLocation'],
             'description': item['description']}
        self.writer.writerow({k:v.encode('utf8') for k,v in D.items()})
        
        return item

    def close_spider(self, spider):
        self.file.close()
