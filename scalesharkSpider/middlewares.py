# -*- coding: utf-8 -*-
from scrapy import log
from proxy import PROXIES
from agents import AGENTS
from changeProxy import ChangeProxy

import random

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

class CustomHttpProxyMiddleware(object):
    # def __init__(self):
    #     changeProxy = ChangeProxy()
    #     changeProxy.getIPData()
    
    def process_request(self, request, spider):
        p = random.choice(PROXIES)
        try:
            request.meta['proxy'] = p['prtcl_ip_port']
            # request.meta['proxy'] = 'https://129.213.76.9:3128'
            print("ip proxy: " + request.meta['proxy'])
        except Exception, e:
            log.msg("Exception %s" % e, _level=log.CRITICAL)
            
    
class CustomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        print("User-Agent: " + agent)
        request.headers['User-Agent'] = agent
