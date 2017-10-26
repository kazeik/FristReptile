#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
'''
爬虫 解析江西省公共资源交易网--鹰潭市政府网站数据
auther:kazeik.chen
date:2017-10-26
'''
import urllib2
import sys
from bs4 import BeautifulSoup


def getHtmlText():
    print('---开始读取html文件 ----')
    url = "http://ytggzy.jiangxi.gov.cn/ytzbw/jyxx/002004/002004001/"
    moreUrl = 'http://ytggzy.jiangxi.gov.cn/ytzbw/jyxx/002004/002004001/MoreInfo.aspx?CategoryNum=002004001'
    response = urllib2.urlopen(url, timeout=5)
    f = response.read()
    return f

def parserHtml(html):
    soup = BeautifulSoup(html, 'lxml', from_encoding='utf-8')
    har = soup.select('.liebiaobg')
    har = str(har)
    subsoup = BeautifulSoup(har, 'lxml', from_encoding='utf-8')
    address = subsoup.select('font')
    adata = subsoup.select('td')
    atext = subsoup.select('td a')

    for child in atext:
        print('-----------')
        body_title = child.get_text()
        alink = 'http://ytggzy.jiangxi.gov.cn' + child['href']
        print(body_title + "\n" + alink)

    for datachild in adata:
        print('============')
        print datachild.get_text()

    for add in address:
        print('<<-->>')
        print add.get_text()

if __name__ == '__main__':
    tempHtml = getHtmlText()
    parserHtml(tempHtml)
    pass
