# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 13:25:11 2018

@author: Bangun
"""

#SCRAPING WEB PAGE

import requests

r = requests.get('http://www.nellanelwan.com/feeds/2290724011173111145/comments/default')

print(r.status_code)

print(r.text)