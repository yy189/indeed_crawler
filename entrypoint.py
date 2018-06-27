from scrapy.cmdline import execute
from search_terms import generate_urls

# generate_urls()
execute(['scrapy', 'crawl', 'indeedSpider'])
