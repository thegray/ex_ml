# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 19:53:20 2018

@author: Bangun
"""

import pandas as pd

# cara ribet pake dict
#d = {'Mayue':3000, 'Lilin':4500, 'Wuyun':8000}

#s = pd.Series(d, name='pay')
#s.index.name = 'name'
#s.reset_index()

#######

# cara mudah, pake list of list or list of tuple

d = [['Mayue',3000],['Lilin',4500], ['Wuyun',8000]]
df = pd.DataFrame(d)
df.index = range(0,3)
df.columns = ['name','pay']

#########

# add a column
df['tax'] = [0.05, 0.05, 0.1]

# add rows 
# add new row with index 5
df.loc[5] = {'name':'Liuxi', 'pay':5000, 'tax':0.05}

# delete data, del or drop (drop is safer)

df.drop(5)  # drop row with index 5

# drop column

df.drop('tax', axis = 1)

# each drop operation return new object, so the original one wont changed

# modify column
df['tax'] = 0.03

# modify row
df.loc[5] = ['Liuxi', 9000, 0.05]
