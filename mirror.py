#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup


def midland():
    url = 'http://www.midland-sq-cinema.jp/'
    r = requests.get(url)
    s = BeautifulSoup(r.text, 'lxml')
    html = s.select('#topics_area')[0].prettify()
    with open('html/midland.html', 'w') as f:
        f.write(html)


if __name__ == '__main__':
    midland()
