# webCrawler

使用：

打开terminal，启动redis-server: $ redis-server
新建一个窗口，启动redis-cli (client): $ redis-cli -a redistest （redistest是connection name）
再新建一个窗口，进入到spider所在目录，执行scrapy爬虫: $ scrapy runspider crunchbaseSpider.py (可开多个这样的窗口进行分布式爬虫)
在redis-cli的窗口输入 $ lpush crunchbaseSpider:start_urls https://www.crunchbase.com/search/organization.companies


要干的活:

- 下一页

- 写安装依赖包 pip install -r requirements.txt




已解决的问题：

- 如果出现 Creating Server TCP listening socket *:6379: bind: Address already in use， 杀进程：

查看redis pid：
$ ps -ef | grep -i redis
  501 17838     1   0 10:27AM ??         0:02.14 redis-server *:6379
  501 19458 19125   0 11:19AM ttys000    0:00.00 grep -i redis

发现pid是17838，杀掉它！
$ kill -9 17838

重新启动redis server：
$ redis-server

done!
