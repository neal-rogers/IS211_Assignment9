#!usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

def url_download(url):
    get_data = requests.get(url)
    return get_data.content

def process_html(html_data):
    print 'Top Players (By Touchdown)'

if __name__ == '__main__':
    link = 'http://www.cbssports.com/nfl/stats/playersort/nfl/year-2016-season-regular-category-touchdowns'
    html = url_download(link)