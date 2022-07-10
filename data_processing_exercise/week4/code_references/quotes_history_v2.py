# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 20:11:33 2018

@author: Bangun
"""

import requests
import re
import json
import pandas as pd
from datetime import date

def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]

quotes = retrieve_quotes_historical('IBM')
list1 = []
for i in range(len(quotes)):
    x = date.fromtimestamp(quotes[i]['date'])
    y = date.strftime(x,'%Y-%m-%d')
    list1.append(y)
quotesdf_ori = pd.DataFrame(quotes, index = list1)
quotesdf = quotesdf_ori.drop(['date'], axis = 1)
#print(quotesdf)

##########

quotes2 = retrieve_quotes_historical('AXP')
df2 = pd.DataFrame(quotes2)
df2.to_csv('stockAXP.csv')

res = pd.read_csv('stockAXP.csv')
print(res['high'])