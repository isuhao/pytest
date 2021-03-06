# encoding: utf-8
'''
获取西祠代理前10页的ip


'''
import requests
from bs4 import BeautifulSoup
import time
import threading

def filter_speed(self,speed):
    speed = speed.replace(u'秒','')
    return float(speed)

def filter_life(self,life):
    '''
                    过滤存活时间
    '''
    life = life.replace(u'天','')
    return life

def is_valid_time(self,life):
    '''
                    判断是否是有效的时间
    '''
    if life.rfind(u'分')>=0 or life.rfind(u'时')>=0:
        return False
    else:
        return True  

def getUrl(baseurl, file, url,proxy,threadno):
    for i in range(threadno+1, threadno+10):
        url = baseurl + areastr(i)
        print url
        trs = get_proxy_msg(url,proxy)
        responseHandler(trs, file)
        time.sleep(10)

def responseHandler(trs,file):
    if trs:
        for i in range(1,len(trs)):
        ##for i in range(1, 2):
            tr = trs[i]
            tds = tr.select('td')
            ##print tds
            td = tds[1]
            ##print td.__class__
            content1 = td.string
            ##print content1.__class__
            ipmsg1 = tds[1].string + ':' + tds[2].string +'\n' ##+ '\t' + tds[8].string
            ##print ipmsg1.__str__()
            file.write(ipmsg1.__str__())
            file.flush()
            ##print ipmsg1.__class__
            ##print ipmsg1
            ##ipmsg2 = tds[6].div.div.get('style')
            ##print ipmsg2.__class__
            ##print ipmsg2

def get_proxy_msg(url,proxy):
    proxy='125.77.80.118:808'
    proxies = {"https": "https://{myproxy}".format(myproxy=proxy)}
    try:
        response = requests.get(url, headers=header, proxies=proxies, timeout=40)
        ##response = requests.get(url, headers=header,  timeout=40)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        soup=BeautifulSoup(response.text,"xml")
        trs = soup.table.select('tr')
        return trs
    except Exception as e:
        print 'http error!'
        print e
    return

##基本蚕食
baseurl="http://www.xicidaili.com/nn/"
header = {'Connection': 'keep-alive',
              'Cache-Control': 'max-age=0',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate, sdch',
              'Accept-Language': 'zh-CN,zh;q=0.8',
              }
file=open('./xici_ip.txt','a')

#开启流程
url=baseurl
fip=open('./xici_ip2.txt','r')
proxys=fip.readlines()
threads=[]
for i in range(2):
    ##getUrl(baseurl, file, url,proxy,threadno):
    proxy=proxys[i]
    threadno=i
    mythread=threading.Thread(target=getUrl,args=(baseurl, file, url, proxy,threadno))
    threads.append(mythread)
    
for t in threads:
    t.start()



file.close()
fip.close()
