#!usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

def process_html(read_data):
    player_stats = []


def main():
    url = 'http://www.cbssports.com/nfl/stats/playersort/nfl/year-2016-season-post-category-touchdowns'
    get_data = urllib2.urlopen(url)
    read_data = BeautifulSoup(get_data.read())

if __name__ == '__main__':
    main()