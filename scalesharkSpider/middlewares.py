# -*- coding: utf-8 -*-
from scrapy import log
from .agents import AGENTS
from .proxy import PROXIES
import random

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

class CustomHttpProxyMiddleware(object):
    def process_request(self, request, spider):
        p = random.choice(PROXIES)
        try:
            request.meta['proxy'] = p['protocol']+'://'+p['ip_port']
            print("ip proxy: " + request.meta['proxy'])
        except Exception as e:
            log.msg("Exception %s" % e, _level=log.CRITICAL)
            
    
class CustomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        print("User-Agent: " + agent)
        request.headers['User-Agent'] = agent
