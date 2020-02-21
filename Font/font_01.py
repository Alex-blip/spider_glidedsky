#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
爬虫-字体反爬-1
字体文件本质上是从字符到图像的一个映射。比如字符0，浏览器会从字体文件当中找到0这个字符对应的图像，然后展示出来。

如果字符0展示并不是0的图像是1的图像呢？这也就意味着爬虫拿到的是字符0，但是人看到的却是图像1。

而我们知道，一切从字符到图像的映射，都可以用来反爬。

这里有一个网站，分了1000页，求所有数字的和。注意，是人看到的数字，不是网页源码中的数字哦~

由于之前的字体服务不太稳定，我们重新开发了一个字体混淆工具。因此，字体文件从woff改成了ttf；以及采用了网页内嵌base64的方式存储字体。之前的爬虫代码需要根据新的网页重新更改下哦~

http://glidedsky.com/level/web/crawler-font-puzzle-1
"""
import re
import xml.dom.minidom
from fontTools.ttLib import TTFont
import requests
import base64
from lxml import etree


class Spider(object):
    def __init__(self, cookie=None):
        self.start_url = 'http://glidedsky.com/level/web/crawler-font-puzzle-1?page=%s'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'glidedsky.com',
            'Pragma': 'no-cache',
            'Cookie': cookie,
            'Referer': 'http://glidedsky.com/level/crawler-basic-1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
        self.total_number = 0

    def send_request(self, url):
        resp = requests.get(url, headers=self.headers)
        return resp.text

    def create_file(self, html_str):
        result = re.search(r'@font-face(.*?)}', html_str, re.S).group(1)
        base64_str = re.search(r'base64,(.*)format', result, re.S).group(1).replace(')', '')
        with open('./font.ttf', 'wb') as f:
            f.write(base64.b64decode(base64_str))

        font = TTFont('font.ttf')
        font.saveXML('font.xml')

    def getMapping(self):
        dict = {
            'zero': '0',
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
        }
        newDict = {}
        dom = xml.dom.minidom.parse('font.xml')
        root = dom.documentElement
        bb = root.getElementsByTagName('GlyphID')
        for j in range(1, 11):
            k = bb[j].getAttribute("name")
            newDict[dict[k]] = str(j - 1)
        return newDict

    def replace_number(self, html_str, newDict):
        html = etree.HTML(html_str)
        div_list = html.xpath('//div[@class="row"]/div')
        for div in div_list:
            release_number_lists = []
            html_numbers = div.xpath('./text()')[0].strip()
            for html_number in html_numbers:
                release_number = newDict[html_number]
                release_number_lists.append(release_number)
            release_numbers = ''.join(release_number_lists)
            self.total_number += int(release_numbers)


if __name__ == '__main__':
    cookie = '_ga=GA1.2.1350307598.1582273218; _gid=GA1.2.1109439363.1582273218; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1582273218,1582274515,1582274528; footprints=eyJpdiI6IlZkUTZSSXByZVplYlwvYmx3d0NmMElRPT0iLCJ2YWx1ZSI6IlwvM0FBUVN0aGRBMUxiZjRQejl1dCtNMitadW8ybVVpS2JSbHhScXB4b1BlNFdcL215bit6YXR2K1lnbEwxY0paayIsIm1hYyI6IjdkMDNhOTIzZTI1NjZlYTIwNzdlZDY2M2Q2NWU0OGZjMjJjODYwOTQwYTFiMDhiMjg4OTdlOTE4MDk4ZGZmN2EifQ%3D%3D; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6InFhM0JJWXBMY0xMQWYwNzQ4RXl5d0E9PSIsInZhbHVlIjoiRFVkaFVhSko3TW5NU1QwRnpLUnRYRCtESExZbDdvNXdXdVF3VHhlYzdZVE52RGJ2ekh0MjE2MkJrYStSbDdLUDFpY3BRaWZLOTV4OG5PK2hQUGJRUGhxcU02Q0ZCWlwvMGhCWlFIdFI2TFFNNHNtbTNRck5xUndMN1dvQ254azgwbHBTemt3cjNjWGZwNGhsR3NiZ0ZvakdROVhTSU1YeHlxK3l4MW5iUmE0TT0iLCJtYWMiOiI1MjgyOWFjM2UxZTYyNTFhMWI0MTNiZDc3Y2Q1OTMxMmY1NTY2MjcxNWE1MDVjNTdjYmRjOTFhNWM2NDk2MDIyIn0%3D; XSRF-TOKEN=eyJpdiI6ImJZVkp5Y2FKTytYa1NPTEFzUWxBSGc9PSIsInZhbHVlIjoiY3NEdFFrQ1Y0S0tIRmkxV0Z3TXVkOXd5MkZIampEamZxQ2hpV0JROHZ1ZXZqUU1cL2IwdmFQVW9DeEtiMzg4YVciLCJtYWMiOiI2OTVmYTMyMzVkNmFkYzQ4Y2E5MTQxZDVjZTI0NWIzNTY2MjkwOWNjN2FlMmFkYzU5NzFiMTE3ODg5YTBiYjBmIn0%3D; glidedsky_session=eyJpdiI6IkpXYjBOUUFYTVJaTGJiMkJDWEtlYVE9PSIsInZhbHVlIjoiWlQ4SldKTWdpYkpSY3AwZEVudXlnY3JOVlwvRkNXWjJCRWJvZlBBbk10ZFQ1TEcxaVI1TzFiVTI0MjY2a1FKeXgiLCJtYWMiOiIwN2M5NjQ5NzIyMTY3ZGJlZmU2YWE5ODY5YTU1YmY0ZTBkYTQ5YmZhZTg2ZmIxOWIxYTUzNzY0NGNjY2MwNGJlIn0%3D; _gat_gtag_UA_75859356_3=1; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1582276123'
    spider = Spider(cookie=cookie)
    url_list = [spider.start_url % i for i in range(1, 1001)]
    for url in url_list:
        print(url)
        html_str = spider.send_request(url)
        spider.create_file(html_str)
        newDict = spider.getMapping()
        spider.replace_number(html_str, newDict)

    print(spider.total_number)
