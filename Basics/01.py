#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from lxml import etree

"""
爬虫的目标很简单，就是拿到想要的数据。

这里有一个网站，里面有一些数字。把这些数字的总和，输入到答案框里面，即可通过本关。
待爬取网站:  http://glidedsky.com/level/web/crawler-basic-1
"""

start_url = 'http://glidedsky.com/level/web/crawler-basic-1'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'glidedsky.com',
    'Pragma': 'no-cache',
    'Cookie': '_ga=GA1.2.1350307598.1582273218; _gid=GA1.2.1109439363.1582273218; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1582273218,1582274515,1582274528; footprints=eyJpdiI6IlZkUTZSSXByZVplYlwvYmx3d0NmMElRPT0iLCJ2YWx1ZSI6IlwvM0FBUVN0aGRBMUxiZjRQejl1dCtNMitadW8ybVVpS2JSbHhScXB4b1BlNFdcL215bit6YXR2K1lnbEwxY0paayIsIm1hYyI6IjdkMDNhOTIzZTI1NjZlYTIwNzdlZDY2M2Q2NWU0OGZjMjJjODYwOTQwYTFiMDhiMjg4OTdlOTE4MDk4ZGZmN2EifQ%3D%3D; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6InFhM0JJWXBMY0xMQWYwNzQ4RXl5d0E9PSIsInZhbHVlIjoiRFVkaFVhSko3TW5NU1QwRnpLUnRYRCtESExZbDdvNXdXdVF3VHhlYzdZVE52RGJ2ekh0MjE2MkJrYStSbDdLUDFpY3BRaWZLOTV4OG5PK2hQUGJRUGhxcU02Q0ZCWlwvMGhCWlFIdFI2TFFNNHNtbTNRck5xUndMN1dvQ254azgwbHBTemt3cjNjWGZwNGhsR3NiZ0ZvakdROVhTSU1YeHlxK3l4MW5iUmE0TT0iLCJtYWMiOiI1MjgyOWFjM2UxZTYyNTFhMWI0MTNiZDc3Y2Q1OTMxMmY1NTY2MjcxNWE1MDVjNTdjYmRjOTFhNWM2NDk2MDIyIn0%3D; XSRF-TOKEN=eyJpdiI6ImJZVkp5Y2FKTytYa1NPTEFzUWxBSGc9PSIsInZhbHVlIjoiY3NEdFFrQ1Y0S0tIRmkxV0Z3TXVkOXd5MkZIampEamZxQ2hpV0JROHZ1ZXZqUU1cL2IwdmFQVW9DeEtiMzg4YVciLCJtYWMiOiI2OTVmYTMyMzVkNmFkYzQ4Y2E5MTQxZDVjZTI0NWIzNTY2MjkwOWNjN2FlMmFkYzU5NzFiMTE3ODg5YTBiYjBmIn0%3D; glidedsky_session=eyJpdiI6IkpXYjBOUUFYTVJaTGJiMkJDWEtlYVE9PSIsInZhbHVlIjoiWlQ4SldKTWdpYkpSY3AwZEVudXlnY3JOVlwvRkNXWjJCRWJvZlBBbk10ZFQ1TEcxaVI1TzFiVTI0MjY2a1FKeXgiLCJtYWMiOiIwN2M5NjQ5NzIyMTY3ZGJlZmU2YWE5ODY5YTU1YmY0ZTBkYTQ5YmZhZTg2ZmIxOWIxYTUzNzY0NGNjY2MwNGJlIn0%3D; _gat_gtag_UA_75859356_3=1; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1582276123',
    'Referer': 'http://glidedsky.com/level/crawler-basic-1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}


def get_html():
    resp = requests.get(start_url, headers=headers)
    return resp


def parse(resp):
    html = etree.HTML(resp.text)
    sum = 0
    div_list = html.xpath('//div[@class="row"]/div')
    for div in div_list:
        number_str = div.xpath('./text()')[0]
        number = int(number_str)
        sum += number
    print(sum)

def run():
    resp = get_html()
    parse(resp)


if __name__ == '__main__':
    run()
