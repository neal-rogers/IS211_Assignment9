#!usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def url_download(url):
    get_data = requests.get(url)
    return get_data.content

def process_html(html_data):
    print 'Top Players (By Touchdown)'


if __name__ == '__main__':
    link = ''
    html = url_download(link)