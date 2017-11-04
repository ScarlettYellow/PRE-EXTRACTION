#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-04 19:49:58
# @Author  : SizheRee (you@example.org)
# @Link    : http://example.org
# @Version : $1.0$

import urllib.request as request
from urllib.error import HTTPError
from queue import Queue
import re
import bs4
import json


class Spider(object):
    '''
    It's a Spider.
    '''
    def __init__(self, name=None, starturl=None, maxpages=20):
        self.name = name
        self.starturl = starturl
        self.urlpool = set()
        self.targeturl = Queue()
        self.maxpages = maxpages
    
    def crwal_recursive(self, url):
        if len(self.urlpool) >= self.maxpages:
            return
#         if the url is repeated, discard.
        if url in self.urlpool:
#             print('find repeated')
            pass
        else:
            try:
                urlop = request.urlopen(url)
                html = urlop.read()
                soup = bs4.BeautifulSoup(html, 'lxml')
            except HTTPError as e:
                print(e)
                return None
            except BaseException as be:
                print(be)
                return None
            else:
                self.urlpool.add(url)
#                 获取文本
            title_content = soup.find(name='h2', id="activity-name")
            main_content = soup.find(name='div',  id="js_content")

            title = title_content.get_text().strip()
            print('title:', title)
            prelist = main_content.find_all(name='p', attrs=None, style=None)
            textlist = []
            for x in prelist:
                text = x.get_text()
                if not text:
                    continue
                text = text.strip('。. ')
                textlist.extend(text.split('。'))
#                 添加到itemdict
                Itemdict[url] = [title, textlist]
#                 获取链接
            try:
                htmlps = soup.find(name='span', text='热门文章推荐').find_parent().find_parent().find_next_siblings(name='p')
#                 有些老网页无法定位
            except AttributeError as e:
                print(e)
#             新网页查找链接
            else:
                count = 0
                for p in htmlps:
                    p_url = p.a.attrs['href']
    #                 print('get new url:\n', p_url)
                    self.targeturl.put(p_url)
                    count += 1
                    if count>10:
                        break
        if self.targeturl.qsize():
            newurl = self.targeturl.get()
            if newurl:
                self.crwal_recursive(newurl)
            else:
                return
        else:
            return
        
if __name__ == '__main__':
    Itemdict = {}
    s = Spider('hhh', 'http://mp.weixin.qq.com/s?__biz=MzA4NzE1NzYyMw==&amp;mid=2247494122&amp;idx=1&amp;sn=89a3d08ac4f656bfc1b8ba97dafa2070&amp;chksm=903f17f2a7489ee4f5714dacbbbebc46e5eb022b1abd53d199873776b6aa35245b87a49242f0&scene=21#wechat_redirect',1000)
    s.crwal_recursive(s.starturl)
    js = json.dumps(Itemdict)
    ob = json.loads(js)