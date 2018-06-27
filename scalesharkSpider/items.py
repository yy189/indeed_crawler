# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.org/en/latest/topics/items.html

from scrapy import Item, Field

class ScalesharkspiderItem(Item):
    job_title = Field()
    company = Field()
    summary = Field()
    job_link = Field()
    company_link = Field()
    location = Field()
    job_id = Field()




