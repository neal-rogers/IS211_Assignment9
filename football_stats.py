#!usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

def url_download(url):
    get_data = requests.get(url)
    return get_data.content

def process_html(html_data):
    player_stats = []
    new_table = html_data.find_all('tr',{'align':'right'})

    for p in player_stats[:20]:
        name = p.contents[0].get_text()
    print player_stats

if __name__ == '__main__':
