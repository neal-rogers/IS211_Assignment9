#!usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup



def main():
    url = 'http://www.cbssports.com/nfl/stats/playersort/nfl/year-2016-season-regular-category-touchdowns'
    get_data = urllib2.urlopen(url)
    read_data = BeautifulSoup(get_data.read())