import scrapy
import xpath
from urls import URLS
import re
from scalesharkSpider.items import ScalesharkspiderItem
import technologies
# from scrapy_redis.spiders import RedisSpider

base_url = 'https://www.indeed.com'

class IndeedSpider(scrapy.Spider):
    name = 'indeedSpider'
    allowed_domains = ['indeed.com']
    start_urls = []
    # redis_key = 'indeedSpider:start_urls'

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(IndeedSpider, self).__init__(*args, **kwargs)

        self.start_urls = URLS


    def parse(self, response):

        job_title_list = response.xpath(xpath.JOBTITLE).extract()
        company_list = response.xpath(xpath.COMPANY).extract()
        summary_list = response.xpath(xpath.SUMMARY).extract()
        job_link_list = response.xpath(xpath.JOBLINK).extract()
        location_list = response.xpath(xpath.LOCATION).extract()
        id_list = response.xpath(xpath.JOBID).extract()[1:]

        for idx, u in enumerate(zip(job_title_list, company_list, summary_list, job_link_list, location_list, id_list)):
            item = ScalesharkspiderItem()
            item['job_title'] = u[0]
            item['company'] = re.sub('<[^<]+?>', '', u[1]).split()[-1]
            item['summary'] = re.sub('<[^<]+?>', '', u[2]).strip()
            item['job_link'] = base_url + u[3]
            item['location'] = u[4]
            item['job_id'] = u[5]

            match = re.search(r'href=[\'"]?([^\'" >]+)', u[1])
            if match:
                company_link = match.group(0)[6:]
                if company_link.startswith("http"):
                    item['company_link'] = company_link
                else:
                    item['company_link'] = base_url + company_link
            else:
                item['company_link'] = 'N/A'

            yield scrapy.Request(item['job_link'], meta={'key': item}, callback = self.parse2)


        next_page_url = response.xpath(xpath.NEXTPAGE).extract()
        if len(next_page_url):
            yield scrapy.Request(base_url+next_page_url[0], callback=self.parse)


    def parse2(self, response):
        item = response.meta['key']
        job_details = response.xpath(xpath.JOB_DETAILS).extract()
        if not len(job_details):
            return
        el_reg = re.findall('[a-z]?[A-Z\.][a-z0-9A-Z#+\.-]*', job_details[0])
        el = list(set(technologies.TECHS_REGEX) & set(el_reg))
        for tech in technologies.TECHS_FOR_LOOP:
            if tech in job_details[0]:
                el.append(tech)
        item['experience_list'] = ", ".join(el)
        yield item
