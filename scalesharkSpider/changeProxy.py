# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import copy_reg
import types

def _pickle_method(m):
    if m.im_self is None:
        return getattr, (m.im_class, m.im_func.func_name)
    else:
        return getattr, (m.im_self, m.im_func.func_name)

copy_reg.pickle(types.MethodType, _pickle_method)

class ChangeProxy(object):
    
    def __init__(self):
        self.num = 300
        self.url = "https://free-proxy-list.net/"
        self.header = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'}

    def get_ips(self):
        with open('proxy.py', 'w') as f:
            f.write('PROXIES = [\n')
            res = requests.get(self.url, headers=self.header)
            soup = BeautifulSoup(res.text, 'lxml')
            tr_list = soup.find_all('tbody')[0].find_all('tr')
            count = 0
            for each in tr_list:
                if count < self.num:
                    ips = each.find_all('td')
                    if ips[6].getText() == 'yes':
                        protocol = 'https'
                    else:
                        protocol = 'http'
                    f.write("\t\t\t{" + "'protocol':'" + protocol + "', 'ip_port':'" + str(ips[0].contents[0]) + ":" + str(ips[1].contents[0]) + "'},\n")
                    count += 1
            f.write(']')
        print('proxy list up-to-date!')

# if __name__ == "__main__":
#     cp = ChangeProxy()
#     cp.get_ips()