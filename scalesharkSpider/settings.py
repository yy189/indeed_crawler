# -*- coding: utf-8 -*-

# Scrapy settings for scalesharkSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scalesharkSpider'

SPIDER_MODULES = ['scalesharkSpider.spiders']
NEWSPIDER_MODULE = 'scalesharkSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scalesharkSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}


# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'scalesharkSpider.middlewares.ScalesharkspiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'scalesharkSpider.middlewares.ScalesharkspiderDownloaderMiddleware': 543,
   # 'scalesharkSpider.middlewares.CustomHttpProxyMiddleware': 543,
   # 'scalesharkSpider.middlewares.CustomUserAgentMiddleware': 545,
   'scrapy.downloadermiddlewares.retry.RetryMiddleware': 351,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scalesharkSpider.extensions.RedisSpiderSmartIdleClosedExensions': 500,
   # 'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'scalesharkSpider.pipelines.ScalesharkspiderPipeline': 300,
   # 111'scrapy_redis.pipelines.RedisPipeline':400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# 自动限速
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 111SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 111DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 111SCHEDULER_PERSIST = True
# Priority
# 111SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
# FIFO
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'
# LIFO
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'

# REDIS_HOST = 'localhost'
# REDIS_PORT = 6379

# 111REDIS_URL = 'redis://@localhost:6379'

# MYEXT_ENABLED=True      # 是否启用扩展，启用扩展为 True， 不启用为 False
# IDLE_NUMBER=360           # 关闭爬虫的持续空闲次数，持续空闲次数超过IDLE_NUMBER，爬虫会被关闭。默认为 360 ，也就是30分钟，一分钟12个时间单位

# MONGODB_HOST = "127.0.0.1"
# MONGODB_PORT = 27017
# MONGODB_DBNAME = "ScaleShark"
# MONGODB_SHEETNAME = "Indeed"