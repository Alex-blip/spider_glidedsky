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
    'Cookie': 'Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1578627987; _ga=GA1.2.1440619268.1578627987; _gid=GA1.2.1333187343.1578627987; footprints=eyJpdiI6IlkybVdLZGJqR2R0YnRYUkZvNmNLdkE9PSIsInZhbHVlIjoiUmViVDZFbVVVdk96VHEzSmNsVFA1Q3VPYTFyZ0VCTDEzeHNiUkE2NGhVV2w2bndqS3ZZcUhaQ0NHU0JHSWtwUSIsIm1hYyI6ImJkYTNlN2MxOTZhODJjYjM3ODc0MzYzNDliMDRkMjhjYjJmZjU0YjI2MTc3ZTZhNTI2NGI5ZmYxYzc1ZGE5NTEifQ%3D%3D; _gat_gtag_UA_75859356_3=1; XSRF-TOKEN=eyJpdiI6ImFDamF5b2t3UFNOTzdHRWlGa01KMFE9PSIsInZhbHVlIjoiU2RHSlJqa1NIR0tVbVJTTTdGZHZRUVRBc2FJcDBFTkl2MWFReEZaZU5hdllHTHhVbEhORUZUZFpVeTNwM3pMRiIsIm1hYyI6ImI0YWFkOGE2OTMzY2M5MjJhY2NlODlhODMwODgwYWUzYzZkMmQxNDk5ZjUwNThiMTQwZTVlNTU1MDYwYzlhYmYifQ%3D%3D; glidedsky_session=eyJpdiI6IkFcL2xIdTREUVhlMWVDNWI2b0ozNUlRPT0iLCJ2YWx1ZSI6IlpySytycDVpTUJES0NXd2dFOW9xZ0ZTZlwvamcrbkpTVkE1SWRNMCtsNnhTeEpXQmFya3RcL0w0WGpnUDNPZThQZCIsIm1hYyI6ImY4NzNlOGI1OWMzYjU3NWZjMWExYTQyYjMyYjFlY2IwYTU4NGM0MmMzZTExNTA4N2RhODdiNjgzYTNhMjEzOGUifQ%3D%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1578652506',
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
