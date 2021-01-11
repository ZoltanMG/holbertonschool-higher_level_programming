#!/usr/bin/python3
import urllib.request
from sys import argv

with urllib.request.urlopen(argv[1]) as response:
    dict_html = response.info()
    if 'X-Request-Id' in dict_html:
        print(dict_html['X-Request-Id'])
