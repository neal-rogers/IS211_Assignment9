#!usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def url_download(url):
    get_data = requests.get(url)
    return get_data.content

def process_html(html_data):
    print 'Top Players (By Touchdown)'
    output = '{:^17} --- {:^3} --- {:^3}'
    soup = BeautifulSoup(webpage, 'html.parser')
    table = soup.find_all(class_={'row1', 'row2'})

    for row in table:
        print output.format(row.contents[0].text, row.contents[2].text, row.contents[6].text)

if __name__ == '__main__':
    link = 'http://www.cbssports.com/nfl/stats/playersort/nfl/year-2016-season-regular-category-touchdowns'
    html = url_download(link)