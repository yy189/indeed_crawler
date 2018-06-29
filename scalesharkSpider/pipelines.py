# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class ScalesharkspiderPipeline(object):
    def __init__(self):
        self.file = open('startups.csv', 'w')
        fieldnames = ['job_id', 'job_title', 'company', 'location', 'summary', 'job_link', 'company_link', 'desired_experience']
        self.writer = csv.DictWriter(self.file, fieldnames=fieldnames)
        self.writer.writeheader()

    def process_item(self, item, spider):
        D = {'job_id': item['job_id'],
             'job_title': item['job_title'],
             'company': item['company'],
             'location': item['location'],
             'job_title': item['job_title'],
             'summary': item['summary'],
             'job_link': item['job_link'],
             'company_link': item['company_link'],
             'desired_experience': item['experience_list']
        }

        self.writer.writerow({k:v.encode('utf8') for k,v in D.items()})
        
        return item

    def close_spider(self, spider):
        self.file.close()