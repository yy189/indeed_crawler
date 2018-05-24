import requests
from bs4 import BeautifulSoup

class ChangeProxy(object):
    
    def __init__(self):
        self.num = 300
        self.url = "https://free-proxy-list.net/"
        self.header = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'}
        # self.Lock = threading.Lock()
        # self.ip_list = []
        
        self.count = 0
        self.evecount = 0
        
    def getIPData(self):
        # del self.ip_list [:]
        res = requests.get(self.url, headers=self.header)
        soup = BeautifulSoup(res.text, 'lxml')
        tr_list = soup.find_all('tbody')[0].find_all('tr')
        count = 0
        with open("proxy.py", "w") as f:
            f.write("PROXIES = [\n")
            for each in tr_list:
                if count < self.num:
                    ips = each.find_all('td')
                    if ips[6].getText() == 'yes':
                        prtcl = "https"
                    else:
                        prtcl = "http"
                    prtcl_ip_port = prtcl + "://" + str(ips[0].contents[0]) + ":" + str(ips[1].contents[0])
                    f.write("\t\t\t{" + "'prtcl_ip_port':'" + prtcl_ip_port + "'},\n")
                    count += 1
            f.write("]\n")
        f.close()
    
    # def changeProxy(self, request):
    #     request.meta["proxy"] = self.ip_list[self.count-1]["prtcl"] + "://" + self.ip_list[self.count-1]["ip_port"]
    #
    # def verify(self):
    #     requests.get(url=self.temp_url, proxies={self.ip_list[self.count-1]["prtcl"]: self.ip_list[self.count-1]["ip_port"]}, timeout=5)
    #
    # def ifUsed(self, request):
    #     try:
    #         self.changeProxy(request)
    #         self.verify()
    #     except:
    #         if self.count == 0 or self.count == 10:
    #             self.getIPData()
    #             self.count = 1
    #         self.evecount = 0
    #         self.count = self.count + 1
    #         self.ifUsed(request)
    #
    # def process_request(self, request, spider):
    #     if self.count == 0 or self.count == 10:
    #         self.getIPData()
    #         self.count = 1
    #
    #     if self.evecount == 3:
    #         self.count = self.count + 1
    #         self.evecount = 0
    #     else:
    #         self.evecount = self.evecount + 1
    #
    #     self.ifUsed(request)

if __name__ == "__main__":
    changeProxy = ChangeProxy()
    changeProxy.getIPData()
