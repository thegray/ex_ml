# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:10:44 2018

@author: Bangun
"""

import requests
import re
import pandas as pd

def retrieve_dji_list():
    r = requests.get('http://money.cnn.com/data/dow30/')
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*<span.*">(.*)<\/span>.*\n.*class="wsod_stream">(.*)<\/span>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    dji_list = []
    for item in dji_list_in_text:
        dji_list.append([item[0], item[1], float(item[2])])
    return dji_list

dji_list = retrieve_dji_list()
djidf = pd.DataFrame(dji_list)
cols = ['code', 'name', 'lasttrade']
djidf.columns = cols
print(djidf)

x = djidf.code
y = djidf.lasttrade
import matplotlib.pyplot as plt
plt.plot(x,y)