# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 20:33:14 2018

@author: Bangun
"""

# word frequency counter

## using Counter() function

import collections
import copy
s = "I am a test sentence and I am very cute."
s_list = s.split() 
s_list_backup = copy.deepcopy(s_list)
[s_list.remove(item) for item in s_list_backup if item in ',.!"']

print(collections.Counter(s_list))

## using dictionary

s_list = s.split()
s_dict = {}
for item in s_list:
    if item.strip() not in ',.!"':
        if item not in s_dict:
            s_dict[item] = 1
        else:
            s_dict[item] += 1
print(s_dict)